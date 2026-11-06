# Risk-Adjusted Return Ratios (Sharpe, Sortino, Omega, Calmar, Martin)

A quick reference for the risk-adjusted return metrics commonly used to compare trading systems or
income-focused ETFs (e.g. covered-call/options-income funds like SPYI/QQQI) beyond simple total return.

> **Disclaimer:** Any specific ratio values shown below (e.g. in the comparison table) are illustrative
> approximations from a point-in-time comparison, not live data — recompute from current returns before
> relying on them, and treat all ratios as one input among many, not a complete risk assessment.

## 1. Sharpe Ratio

**What it measures:** Return per unit of *total* volatility (risk).

**What it means:** Uses total volatility (both up and down moves) and penalizes upside volatility the
same as downside.

**Interpretation:** Roughly, > 1.0 is considered good and > 2.0 very good — higher is better.

**Limitation:** Treats upside and downside volatility equally, which isn't ideal for income or
asymmetric-payoff strategies.

## 2. Sortino Ratio

**What it measures:** Return per unit of *downside* risk only.

**What it means:** Only penalizes negative volatility, so it tends to read better than Sharpe for
income strategies and trend-following systems where upside volatility dominates.

**Interpretation:** Higher is better.

**Limitation:** Still a volatility-based measure — it doesn't account for drawdown depth or duration.

## 3. Omega Ratio

**What it measures:** Probability-weighted gains vs. losses relative to a threshold return.

**What it means:** Captures the full return distribution (including skewness and fat tails), not just
variance, so it's more complete than Sharpe in principle.

**Interpretation:** > 1.0 is favorable (more weighted gains than losses); higher is better.

**Limitation:** Less intuitive and less commonly reported than Sharpe/Sortino.

## 4. Calmar Ratio

**What it measures:** Return relative to maximum drawdown.

**What it means:** Focuses on the single worst peak-to-trough loss — relevant for traders and leveraged
strategies where surviving the worst drawdown matters most.

**Interpretation:** > 1.0 is considered strong; higher means better recovery relative to the worst loss.

**Limitation:** Uses only the single worst drawdown and ignores volatility elsewhere in the series.

## 5. Martin Ratio (Ulcer Performance Index)

**What it measures:** Return adjusted for drawdown "pain" — both depth *and* duration (via the Ulcer
Index).

**What it means:** Penalizes prolonged underwater periods, which arguably makes it a more realistic
measure of the psychological difficulty of holding a strategy through a drawdown.

**Interpretation:** Higher means a smoother recovery and a less stressful equity curve.

**Limitation:** Less widely reported than the other ratios above.

## Quick Comparison

| Ratio   | Penalizes                 | Best for                        |
| ------- | -------------------------- | -------------------------------- |
| Sharpe  | Total volatility           | General portfolio comparison     |
| Sortino | Downside volatility        | Income & trend-following systems |
| Omega   | Distribution skew          | More complete risk analysis      |
| Calmar  | Max drawdown               | Traders / leveraged strategies   |
| Martin  | Drawdown depth + duration  | Realistic "pain" measurement     |

**Simple intuition:**

* Sharpe → "How smooth is the ride?"
* Sortino → "How bad are the down moves?"
* Omega → "Do gains outweigh losses overall?"
* Calmar → "How bad was the worst crash?"
* Martin → "How long and deep was the pain?"

### See Also

* [Position Sizing for Day Trading](position_sizing.html)
* [Class 9 - Backtesting & Strategy](../class9_backtesting_strategy.html) — the performance report a
  backtester prints typically includes CAGR, Sharpe, and max drawdown.
* [Risk Management Deep Dive Hub](index.html)
