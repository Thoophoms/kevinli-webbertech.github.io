# Python Risk & Position Size Calculator

A standalone command-line tool ([python_risk_calculator.py](python_risk_calculator.py)) that implements the
[position sizing formulas](position_sizing.html)
for stocks, ATR-based stops, futures, and options, plus batch CSV processing and a daily risk-cap check.

> **Disclaimer:** This tool performs arithmetic only — it does not place trades, pull live quotes, or account for
> commissions/slippage/taxes. Verify outputs before sizing real trades.

## Usage

* Stock sizing:

```
python python_risk_calculator.py stock --account 25000 --risk 0.01 --entry 50 --stop 49.5
```

* ATR-based sizing:

```
python python_risk_calculator.py atr --account 25000 --risk 0.01 --entry 50 --atr 0.4 --mult 1.5
```

* Futures sizing:

```
python python_risk_calculator.py futures --account 50000 --risk 0.01 --point_value 50 --stop_points 4
```

* Options sizing:

```
python python_risk_calculator.py option --account 20000 --risk 0.01 --premium 2.0
```

* Batch CSV mode (requires `pandas`, columns depend on `--mode`: e.g. `entry,stop` for stock, `entry,atr` for atr, `point_value,stop_points` for futures, `option_premium` for option):

```
python python_risk_calculator.py batch --input trades.csv --output results.csv --mode stock --account 25000 --risk 0.01
```

## See Also

* [Position Sizing for Day Trading](position_sizing.html) — the formulas this script implements.
* [Class 9 - Backtesting & Strategy](../class9_backtesting_strategy.html) — validate an idea with history before sizing it.
* [Risk Management Deep Dive Hub](index.html)
