# Kelly Criterion — Formula & Examples

The Kelly Criterion is a formula for sizing bets (or trades) to maximize the long-run geometric growth
rate of capital, given a known or estimated edge. It was developed by John Kelly Jr. at Bell Labs in 1956,
originally for signal-noise problems, and later adopted by gamblers and investors (most famously Edward
Thorp) for bet/position sizing.

> **Disclaimer:** The Kelly Criterion assumes you know your true win probability and payoff ratio — in
> real trading these are *estimates*, not known constants. Overestimating your edge and betting full Kelly
> is a well-documented way to blow up an account; most practitioners use a fraction of Kelly (see below).
> This page is educational, not personalized financial advice.

## The Formula

### General (odds) form

```
f* = (bp - q) / b
```

Where:

* `f*` = fraction of capital to wager/invest
* `b` = net odds received on the bet (i.e., win $b for every $1 risked)
* `p` = probability of winning
* `q` = probability of losing = `1 - p`

### Simplified trading form

For a strategy with a win rate and an average win/loss ratio, the same formula is often written as:

```
f* = W - (1 - W) / R
```

Where:

* `W` = win rate (probability of a winning trade)
* `R` = average win size ÷ average loss size (the payoff ratio — same concept as the
  [risk/reward ratio](risk_reward_ratio.html), inverted)

Both forms are equivalent; the trading form just substitutes `b = R`, `p = W`, `q = 1 - W`.

## Example 1 — Coin Flip (Classic)

A biased coin wins 60% of the time, paying 1:1 (bet $1, win $1 or lose $1).

```
p = 0.60, q = 0.40, b = 1
f* = (1 × 0.60 − 0.40) / 1 = 0.20
```

**Kelly says bet 20% of your bankroll per flip.** Betting more than this reduces long-run growth even
though each individual flip still has positive expectancy; betting less simply grows the bankroll slower.

## Example 2 — Day Trading Strategy

A strategy wins 45% of trades, with average winners 2.5× the size of average losers (R = 2.5).

```
W = 0.45, R = 2.5
f* = 0.45 − (1 − 0.45) / 2.5 = 0.45 − 0.22 = 0.23
```

**Full Kelly ≈ 23% of account risked per trade** — in practice this is far more aggressive than the
0.5%–1% per-trade guidelines in [Position Sizing for Day Trading](position_sizing.html),
which is exactly why most traders use a fraction of Kelly (see below), not full Kelly.

## Example 3 — Negative Edge (Kelly Says Don't Bet)

A strategy wins only 30% of trades with a 1:1 payoff (R = 1):

```
f* = 0.30 − (1 − 0.30) / 1 = 0.30 − 0.70 = −0.40
```

A negative `f*` means there is no positive edge at this payoff ratio — Kelly's answer is **don't take this
bet at all** (or, in trading terms, the setup needs a better win rate or a better risk/reward ratio before
sizing a position into it).

## Half-Kelly and Fractional Kelly

Full Kelly sizing is mathematically "optimal" for long-run growth **only if your edge estimates (`W` and
`R`) are exactly correct** — and they rarely are. Because real-world edge estimates are noisy, and because
full Kelly implies large, psychologically brutal drawdowns even when the edge is real, most practitioners
use a fraction of the full Kelly number:

| Fraction | Trade-off |
|---|---|
| **Full Kelly (100%)** | Maximizes theoretical long-run growth rate; also maximizes volatility/drawdown risk if edge estimates are even slightly wrong |
| **Half-Kelly (50%)** | Commonly used compromise — captures most of the growth benefit with meaningfully smaller drawdowns |
| **Quarter-Kelly (25%)** | Conservative; popular for live trading where edge estimates are uncertain or sample sizes are small |

Using Example 2 above (full Kelly ≈ 23%), half-Kelly would size the position at **~11.5%** of the account
and quarter-Kelly at **~5.75%** — still aggressive relative to the fixed 0.5%–1% rules used elsewhere in
this course, which is a reminder that Kelly sizing and fixed-percent risk rules are two different
frameworks; most retail traders lean toward the fixed-percent approach specifically because it does not
require a reliable estimate of `W` and `R` for every strategy.

## Key Caveats

* **Garbage in, garbage out:** Kelly sizing is only as good as your `W` and `R` estimates. Small samples
  (a few dozen trades) produce unreliable estimates — see
  [Class 9 - Backtesting & Strategy](../class9_backtesting_strategy.html) for
  validating a strategy's actual win rate and payoff ratio before sizing off of it.
* **Assumes a single repeated bet:** Real portfolios have correlated positions, changing market regimes,
  and non-stationary edges — the classical formula does not account for any of that.
* **Volatility vs. ruin:** Even with a correct positive edge, full Kelly can produce drawdowns of 50%+ along
  the way. Fractional Kelly exists specifically to trade some growth rate for a smoother equity curve.

### See Also

* [Position Sizing for Day Trading](position_sizing.html)
* [Risk/Reward Ratio: Day Trading vs. Swing Trading](risk_reward_ratio.html)
* [Risk-Adjusted Return Ratios](risk_adjusted_return_ratios.html)
* [Expected Utility](expected_utility.html) — the decision-theory reason traders often size below full Kelly.
* [Risk Management Deep Dive Hub](index.html)
