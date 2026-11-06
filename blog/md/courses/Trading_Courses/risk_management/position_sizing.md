# Position Sizing for Day Trading

A concise, practical day-trading position sizing plan focused on risk management.

> **Disclaimer:** These are general risk-management guidelines, not personalized financial advice. Position limits, risk tolerance, and broker/pattern-day-trading rules vary — confirm against your own account size, broker, and tax/regulatory situation before trading.

---

## 1. Core Risk Rules (simple & professional)

**Account Risk per Trade**

* Risk **0.5% – 1%** of total account per trade
* Beginners: **0.25% – 0.5%**
* Aggressive day traders: **1% max**

**Daily Risk Cap**

* Stop trading for the day after **-2% to -3%** account loss

**Max Concurrent Risk**

* Total open risk should not exceed **2–3%** of account

---

## 2. Position Size Formula (the engine)

This is the key formula:

```
Position Size (shares/contracts) =
    (Account Balance × Risk %) ÷ Stop Loss Distance
```

Where:

* **Account Balance** = your current equity
* **Risk %** = % you’re risking per trade
* **Stop Loss Distance** = (Entry Price – Stop Price)

---

## 3. Stock Day Trading Example

**Account:** $25,000
**Risk per trade:** 1% → $250
**Trade idea:**

* Entry = $50.00
* Stop-loss = $49.50
* Risk per share = $0.50

**Position size:**

```
$250 ÷ $0.50 = 500 shares
```

✅ You buy **500 shares**
✅ If stopped out, loss ≈ $250

---

## 4. Futures Position Sizing Example

**Account:** $50,000
**Risk per trade:** 1% → $500
**Instrument:** E-mini S&P 500 (ES)

* Risk per point = $50
* Stop loss = 4 points

```
Risk per contract = 4 × $50 = $200
Contracts = $500 ÷ $200 = 2 contracts
```

✅ Trade **2 ES contracts**

---

## 5. Options Position Sizing Example

Position size is based on **total premium risked**, not contract face value.

**Account:** $20,000
**Risk per trade:** 1% → $200
**Option price:** $2.00 = $200 per contract

✅ Trade **1 contract max**

---

## 6. ATR-Based Smart Stops (Pro Traders Use This)

Instead of random stops, use **ATR-based stop losses**:

```
Stop distance = ATR × multiplier
```

Example:

* ATR(14) = $0.40
* Multiplier = 1.5

```
Stop distance = $0.40 × 1.5 = $0.60
```

Then use it in the position size formula.

---

## 7. Daily Loss Cutoff Plan

A professional day trading “kill switch”:

| Scenario        | Rule                     |
| --------------- | ------------------------ |
| 1 losing trade  | reduce size by 50%       |
| 2 losing trades | stop trading for the day |
| 3 losing trades | mandatory day off        |

---

## 8. Scaling Positions (for strong setups)

Only scale **after partial profit locked**:

Example:

* Take half off at **1R** (risk unit)
* Move stop to breakeven
* Let the rest ride

---

## 9. Quick Position Size Cheat Table

| Account Size | 0.5% Risk | 1% Risk |
| ------------ | --------- | ------- |
| $10,000      | $50       | $100    |
| $25,000      | $125      | $250    |
| $50,000      | $250      | $500    |
| $100,000     | $500      | $1,000  |

---

## 10. Golden Rules

* Stops **always placed at trade entry**
* Never move stop farther away
* Size based on **risk, not confidence**
* Survive first — profits come later

---

### See Also

* [Python Risk Calculator](python_risk_calculator.html) — CLI tool implementing the stock/ATR/futures/options formulas above.
* [Risk-Adjusted Return Ratios](risk_adjusted_return_ratios.html) — Sharpe, Sortino, Omega, Calmar, Martin.
* [Kelly Criterion — Formula & Examples](kelly_criterion.html) — an alternative, edge-based sizing framework.
* [Day Trading Rules & Discipline](day_trading_rules.html)
* [Risk Management Deep Dive Hub](index.html)
