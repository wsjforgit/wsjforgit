#!/usr/bin/env python3
import argparse, csv
from pathlib import Path

EXPECTED_ITEMS=24

def classify(total):
    if total <= 16: return "demo-grade"
    if total <= 32: return "usable with active supervision"
    if total <= 42: return "production-oriented"
    return "mature baseline; continue adversarial testing"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("scorecard",type=Path)
    args=ap.parse_args()
    with args.scorecard.open(newline="",encoding="utf-8-sig") as f:
        rows=list(csv.DictReader(f))
    if len(rows)!=EXPECTED_ITEMS:
        raise SystemExit(f"Expected {EXPECTED_ITEMS} items, found {len(rows)}")
    total=0; incomplete=[]; by_section={}
    for i,row in enumerate(rows,start=2):
        raw=(row.get("score_0_2") or "").strip()
        if not raw:
            incomplete.append(i); continue
        try: score=int(raw)
        except ValueError: raise SystemExit(f"Row {i}: score must be 0, 1, or 2")
        if score not in (0,1,2): raise SystemExit(f"Row {i}: score must be 0, 1, or 2")
        total += score
        by_section.setdefault(row.get("section","Uncategorized"),[]).append(score)
    if incomplete:
        raise SystemExit("Incomplete score rows: "+",".join(map(str,incomplete)))
    print(f"TOTAL={total}/48")
    print(f"MATURITY={classify(total)}")
    for sec,vals in by_section.items():
        print(f"SECTION {sec}={sum(vals)}/{2*len(vals)}")
if __name__=="__main__": main()
