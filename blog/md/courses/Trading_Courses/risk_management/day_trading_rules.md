# Day Trading Rules & Discipline

Operational and discipline rules to apply on top of the trade-level math in
[Position Sizing](position_sizing.html) and
[Risk/Reward Ratio](risk_reward_ratio.html).

> **Disclaimer:** These are general discipline guidelines, not rules of any specific broker or
> prop-trading firm. Confirm actual limits (daily loss caps, max contracts, pattern-day-trading rules,
> etc.) against your own broker/firm agreement.

## Daily Discipline Rules

A simple "kill switch" framework used by many disciplined day traders / prop-style accounts to cap
variance:

| Rule                 | Typical Limit             |
| --------------------- | -------------------------- |
| Max trades/day         | 3                          |
| Max losing trades/day  | 2 (then stop for the day)  |
| Daily stop (loss cap)  | ~1% of account             |
| Walk away after        | ~1.5% gain on the day      |

The idea is low variance over heroics: protect the account's drawdown first, let profits come second.

## Pre-Trade Checklist

Before entering any trade, confirm:

* Trend/bias is aligned on a higher timeframe.
* Price relative to VWAP (or your chosen reference) supports the trade direction.
* A clear, predefined stop-loss level exists.
* Risk per trade is within your plan (commonly 0.25%–1%; see [Position Sizing](position_sizing.html)).
* Risk/reward is at least ~1.5:1–2:1 (see [Risk/Reward Ratio](risk_reward_ratio.html)).

If any of these fail, skip the trade.

## Watch-List Flags

* A $2–$20 premarket price jump (gap) is a common flag to add a symbol to the day's watch list for
  further review — it does not by itself justify a trade.

## Network & Software

Reliable, fast internet is important for day trading. A minimum of 25 Mbps download / 3 Mbps upload is
commonly recommended, with extra weight on download speed since most traders consume more data (charts,
quotes, news) than they send.

## Further Reading

* <https://scanz.com/become-a-better-trader/>
* <https://scanz.com/category/tutorials/>
* <https://www.warriortrading.com/scanners/>

### See Also

* [Position Sizing for Day Trading](position_sizing.html)
* [Risk/Reward Ratio](risk_reward_ratio.html)
* [Stop Order Strategies](stop_order_strategies.html)
* [Risk Management Deep Dive Hub](index.html)
