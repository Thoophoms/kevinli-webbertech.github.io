#!/usr/bin/env python3
"""
risk_calculator.py

Standalone Python Risk & Position Size Calculator for day trading.
Supports:
- Stocks
- ATR-based stops
- Futures
- Options
- Daily risk cap
- Batch CSV processing
"""

import argparse
import csv
from math import floor
from typing import Dict

try:
    import pandas as pd
except Exception:
    pd = None


# ======================
# Core Calculations
# ======================

def position_size_stock(account_balance: float, risk_pct: float, entry: float, stop: float) -> Dict:
    risk_amount = account_balance * risk_pct
    risk_per_share = abs(entry - stop)

    if risk_per_share <= 0:
        shares = 0
    else:
        shares = floor(risk_amount / risk_per_share)

    position_value = shares * entry
    actual_risk = shares * risk_per_share
    actual_risk_pct = actual_risk / account_balance if account_balance > 0 else 0

    return {
        "account_balance": account_balance,
        "risk_pct_target": risk_pct,
        "risk_amount_target": risk_amount,
        "entry": entry,
        "stop": stop,
        "risk_per_share": risk_per_share,
        "shares": shares,
        "position_value": position_value,
        "actual_risk_amount": actual_risk,
        "actual_risk_pct": actual_risk_pct
    }


def position_size_atr(account_balance: float, risk_pct: float, entry: float, atr: float, atr_mult: float = 1.5) -> Dict:
    stop_distance = atr * atr_mult
    stop_price = entry - stop_distance
    result = position_size_stock(account_balance, risk_pct, entry, stop_price)

    result.update({
        "atr": atr,
        "atr_mult": atr_mult,
        "stop_distance": stop_distance,
        "stop_price": stop_price
    })
    return result


def position_size_futures(account_balance: float, risk_pct: float, point_value: float, stop_points: float) -> Dict:
    risk_amount = account_balance * risk_pct
    risk_per_contract = abs(stop_points) * point_value

    if risk_per_contract <= 0:
        contracts = 0
    else:
        contracts = floor(risk_amount / risk_per_contract)

    actual_risk = contracts * risk_per_contract
    actual_risk_pct = actual_risk / account_balance if account_balance > 0 else 0

    return {
        "account_balance": account_balance,
        "risk_pct_target": risk_pct,
        "risk_amount_target": risk_amount,
        "point_value": point_value,
        "stop_points": stop_points,
        "contracts": contracts,
        "risk_per_contract": risk_per_contract,
        "actual_risk_amount": actual_risk,
        "actual_risk_pct": actual_risk_pct
    }


def position_size_option(account_balance: float, risk_pct: float, option_premium: float) -> Dict:
    risk_amount = account_balance * risk_pct
    risk_per_contract = option_premium * 100

    if risk_per_contract <= 0:
        contracts = 0
    else:
        contracts = floor(risk_amount / risk_per_contract)

    position_cost = contracts * risk_per_contract
    actual_risk_pct = position_cost / account_balance if account_balance > 0 else 0

    return {
        "account_balance": account_balance,
        "risk_pct_target": risk_pct,
        "risk_amount_target": risk_amount,
        "option_premium": option_premium,
        "risk_per_contract": risk_per_contract,
        "contracts": contracts,
        "position_cost": position_cost,
        "actual_risk_pct": actual_risk_pct
    }


def enforce_daily_cap(account_balance: float, trades: list, daily_cap_pct: float) -> Dict:
    total_risk = sum(t.get("actual_risk_amount", 0) for t in trades)
    cap_amount = account_balance * daily_cap_pct

    return {
        "total_risk_amount": total_risk,
        "daily_cap_amount": cap_amount,
        "within_cap": total_risk <= cap_amount,
        "total_risk_pct": total_risk / account_balance if account_balance > 0 else 0
    }


# ======================
# CSV Batch Processing
# ======================

def process_csv(input_csv: str, output_csv: str, mode: str, account_balance: float, risk_pct: float, atr_mult: float = 1.5):
    if pd is None:
        raise RuntimeError("Install pandas to use CSV batch mode: pip install pandas")

    df = pd.read_csv(input_csv)
    results = []

    for _, row in df.iterrows():
        if mode == "stock":
            res = position_size_stock(account_balance, risk_pct, float(row["entry"]), float(row["stop"]))
        elif mode == "atr":
            res = position_size_atr(account_balance, risk_pct, float(row["entry"]), float(row["atr"]), atr_mult)
        elif mode == "futures":
            res = position_size_futures(account_balance, risk_pct, float(row["point_value"]), float(row["stop_points"]))
        elif mode == "option":
            res = position_size_option(account_balance, risk_pct, float(row["option_premium"]))
        else:
            raise ValueError("Invalid mode")

        results.append(res)

    pd.DataFrame(results).to_csv(output_csv, index=False)
    return output_csv


# ======================
# CLI
# ======================

def print_dict(d: Dict):
    for k, v in d.items():
        print(f"{k}: {v}")


def main():
    parser = argparse.ArgumentParser(description="Risk / Position Size Calculator")
    sub = parser.add_subparsers(dest="cmd")

    stock = sub.add_parser("stock")
    stock.add_argument("--account", type=float, required=True)
    stock.add_argument("--risk", type=float, required=True)
    stock.add_argument("--entry", type=float, required=True)
    stock.add_argument("--stop", type=float, required=True)

    atr = sub.add_parser("atr")
    atr.add_argument("--account", type=float, required=True)
    atr.add_argument("--risk", type=float, required=True)
    atr.add_argument("--entry", type=float, required=True)
    atr.add_argument("--atr", type=float, required=True)
    atr.add_argument("--mult", type=float, default=1.5)

    futures = sub.add_parser("futures")
    futures.add_argument("--account", type=float, required=True)
    futures.add_argument("--risk", type=float, required=True)
    futures.add_argument("--point_value", type=float, required=True)
    futures.add_argument("--stop_points", type=float, required=True)

    option = sub.add_parser("option")
    option.add_argument("--account", type=float, required=True)
    option.add_argument("--risk", type=float, required=True)
    option.add_argument("--premium", type=float, required=True)

    batch = sub.add_parser("batch")
    batch.add_argument("--input", required=True)
    batch.add_argument("--output", required=True)
    batch.add_argument("--mode", choices=["stock", "atr", "futures", "option"], default="stock")
    batch.add_argument("--account", type=float, default=100000)
    batch.add_argument("--risk", type=float, default=0.01)
    batch.add_argument("--atr_mult", type=float, default=1.5)

    args = parser.parse_args()

    if args.cmd == "stock":
        print_dict(position_size_stock(args.account, args.risk, args.entry, args.stop))

    elif args.cmd == "atr":
        print_dict(position_size_atr(args.account, args.risk, args.entry, args.atr, args.mult))

    elif args.cmd == "futures":
        print_dict(position_size_futures(args.account, args.risk, args.point_value, args.stop_points))

    elif args.cmd == "option":
        print_dict(position_size_option(args.account, args.risk, args.premium))

    elif args.cmd == "batch":
        output = process_csv(args.input, args.output, args.mode, args.account, args.risk, args.atr_mult)
        print(f"Results saved to {output}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
