# Risk/Reward Ratio: Day Trading vs. Swing Trading

The risk/reward ratio (R/R) is a simple trading metric that compares how much you're willing to lose
(risk) against how much you expect to gain (reward) on a trade.

## Basic Definition

**Example:** Buy a stock at $100, with a stop-loss at $95 (risk = $5) and a take-profit at $115
(reward = $15). That's a risk/reward of **1:3** — you risk $1 to make $3.

## Why It Matters

A good risk/reward ratio lets you stay profitable even with a lower win rate. For example, at a 1:3
risk/reward with a 40% win rate over 10 trades:

* 4 wins × 3R = +12R
* 6 losses × 1R = −6R
* Net = **+6R**

You can lose more often than you win and still make money, as long as your average winner is
large enough relative to your average loser.

## Common Benchmarks

| Risk/Reward | Typical Use                           |
| ----------- | -------------------------------------- |
| 1:1         | Scalping, high win-rate systems        |
| 1:2         | Conservative swing trading             |
| 1:3         | Day trading, trend-following           |
| 1:5+        | Breakouts, long-term trades            |

Most professional traders aim for at least 1:2 or 1:3.

## Risk/Reward vs. Position Size

Risk/reward tells you about *trade quality*, not *how much money* to trade. You still need:

* An account risk per trade (e.g., 1% — see [Position Sizing](position_sizing.html))
* Position sizing based on your stop-loss distance

**Example:** Account = $50,000, risk per trade = 1% ($500), stop-loss = $2/share → position size = 250 shares.

## Day Trading

**Characteristics:** Trades last minutes to hours (closed by end of day); small price moves targeted;
high trade frequency; tight stop-losses.

**Typical risk/reward:** 1:1 to 1:2 — small intraday moves limit the reward per trade, so a higher win
rate is often required.

**Example:** Buy at $100, stop-loss $99.50 (risk $0.50), target $101.50 (reward $1.50) → R/R ≈ 1:3 is an
aggressive intraday target; 1:1–1:2 is more typical given market noise.

**Implication:** Even a 50–60% win rate can be profitable if risk is controlled; position sizing is
often smaller per trade to manage volatility.

## Swing Trading

**Characteristics:** Trades last days to weeks; captures larger trends; fewer trades with larger price
moves; wider stop-losses to avoid being shaken out by daily noise.

**Typical risk/reward:** 1:2 to 1:5+ — the longer time horizon allows a bigger profit potential.

**Example:** Buy at $100, stop-loss $95 (risk $5), target $120 (reward $20) → R/R = 1:4.

**Implication:** Can tolerate a lower win rate (e.g., ~40%) and still be profitable, but each trade
carries more absolute risk, so position sizing is critical.

## Comparison

| Aspect               | Day Trading     | Swing Trading   |
| --------------------- | --------------- | --------------- |
| Trade Duration         | Minutes–Hours   | Days–Weeks      |
| Typical Risk/Reward    | 1:1 – 1:2       | 1:2 – 1:5+      |
| Win Rate Needed        | Higher (50–70%) | Lower (30–50%)  |
| Stop-Loss              | Tight           | Wider           |
| Profit Target          | Small           | Large           |
| Trade Frequency        | High            | Low             |

## Risk/Reward, Win Rate & Expectancy

Risk/reward and win rate combine into **expectancy** — the average expected profit per trade, expressed
in units of risk (R). If expectancy is positive, the system is profitable over a large enough sample;
if negative, it loses money even if individual trades look reasonable.

| Strategy      | Risk/Reward | Win Rate | Notes                              |
| ------------- | ----------- | -------- | ------------------------------------ |
| Day Trading   | 1:1.5       | 60%      | Small wins, higher frequency         |
| Swing Trading | 1:4         | 40%      | Big wins, lower frequency            |

Both rows above work out to positive expectancy despite very different win rates — the point is that a
low win rate with a large R/R can be just as profitable as a high win rate with a small R/R. Visually,
this is often shown as a risk/reward "arrow" diagram: a short arrow down for the stop-loss distance and a
longer arrow up (proportional to the R/R ratio) for the profit target.

## Key Takeaway

Risk/reward measures trade *quality*, not trade frequency. Consistently good R/R combined with disciplined
[position sizing](position_sizing.html) and risk management is
what supports long-term survival as a trader.

### See Also

* [Position Sizing for Day Trading](position_sizing.html)
* [Kelly Criterion — Formula & Examples](kelly_criterion.html) — sizing a position off your win rate and payoff ratio
* [Day Trading Rules & Discipline](day_trading_rules.html)
* [Stop Order Strategies](stop_order_strategies.html)
* [Risk Management Deep Dive Hub](index.html)
