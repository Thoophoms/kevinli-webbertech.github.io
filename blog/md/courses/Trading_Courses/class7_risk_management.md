# Class 7 - Risk Management

## Goal

Protect trading capital, which matters more than any single winning trade.

## Topics

- Position sizing based on account risk percentage
- Stop-loss placement strategies
- Risk/reward ratio and why 1:2 or better is preferred
- Diversification vs. concentration
- The math of drawdowns (why losing 50% requires a 100% gain to recover)

## Definitions

- **Position sizing**: Determining how many shares/contracts to trade based on account size and the amount of capital you are willing to risk.
- **Account risk percentage**: The portion of total trading capital (commonly 1-2%) that a trader is willing to lose on a single trade.
- **Stop-loss**: A predetermined price level at which a losing trade is automatically closed to limit further loss.
- **Risk/reward ratio**: The ratio of potential loss (risk) to potential gain (reward) on a trade, e.g., a 1:2 ratio risks $1 to make $2.
- **Diversification**: Spreading capital across multiple assets or positions to reduce the impact of any single position's loss.
- **Concentration**: Allocating a large portion of capital to a single position or a small number of positions, increasing both potential reward and risk.
- **Drawdown**: The percentage decline from a portfolio's peak value to a subsequent low, used to measure the size of a losing streak.

## Key Takeaways

- Never risk more than 1-2% of trading capital on a single trade.
- A stop-loss should be set before entering the trade, not after.
- Consistent risk management turns a mediocre win rate into a profitable system.

## Position Sizing Formula

```
Dollar risk per trade = Account size x Risk %
Risk per share        = Entry price - Stop-loss price
Position size (shares) = Dollar risk per trade / Risk per share
```

## Worked Example 1: Dollar-based Stop-loss

- Account size: $10,000
- Risk per trade: 1% -> $100
- Entry price: $50.00
- Stop-loss price: $47.50 (a $2.50 per-share risk)

```
Dollar risk per trade = $10,000 x 1% = $100
Risk per share        = $50.00 - $47.50 = $2.50
Position size          = $100 / $2.50 = 40 shares
```

Buy 40 shares. If the stop-loss is hit, the loss is 40 x $2.50 = $100, exactly 1% of the account.

## Worked Example 2: Percentage-based Stop-loss

- Account size: $10,000
- Risk per trade: 1% -> $100
- Entry price: $50.00
- Stop-loss: 5% below entry -> $50.00 x 0.95 = $47.50 (same $2.50 per-share risk as Example 1)

This is the same setup as the Practice question below, just expressed as a percentage stop instead of a fixed dollar stop - both methods agree on 40 shares.

## Worked Example 3: Larger Account, Wider Stop

- Account size: $25,000
- Risk per trade: 2% -> $500
- Entry price: $120.00
- Stop-loss price: $114.00 (a $6.00 per-share risk)

```
Dollar risk per trade = $25,000 x 2% = $500
Risk per share        = $120.00 - $114.00 = $6.00
Position size          = $500 / $6.00 = 83 shares (rounded down)
```

Buy 83 shares (rounding down keeps the actual dollar risk at or below the $500 limit).

## Scenario Table

| Account Size | Risk % | Dollar Risk | Entry Price | Stop-loss Price | Risk/Share | Position Size |
|-------------|--------|-------------|--------------|------------------|------------|----------------|
| $5,000      | 1%     | $50         | $20.00       | $19.00           | $1.00      | 50 shares      |
| $10,000     | 1%     | $100        | $50.00       | $47.50           | $2.50      | 40 shares      |
| $25,000     | 2%     | $500        | $120.00      | $114.00          | $6.00      | 83 shares      |
| $50,000     | 1.5%   | $750        | $75.00       | $72.00           | $3.00      | 250 shares     |

## Practice

1. Calculate the position size for a $10,000 account risking 1% per trade, with a stop-loss 5% below entry.
2. Using the formula above, calculate the position size for a $15,000 account risking 1.5% per trade, entering at $80.00 with a stop-loss at $76.00.
3. An account worth $8,000 wants to risk 2% on a trade entering at $30.00 with a stop-loss at $28.50. How many shares should be bought, and what is the exact dollar amount at risk?

## Further Reading — Risk Management Deep Dive

- [Risk Management Deep Dive Overview](risk_management/index.html)
- [Position Sizing for Day Trading](risk_management/position_sizing.html) — extended formulas for stocks, futures, and options, ATR-based stops, and daily loss cutoffs
- [Python Risk Calculator](risk_management/python_risk_calculator.html) — a CLI tool that implements these position-sizing formulas
- [Risk/Reward Ratio: Day Trading vs. Swing Trading](risk_management/risk_reward_ratio.html)
- [Day Trading Rules & Discipline](risk_management/day_trading_rules.html)
- [Stop Order Strategies](risk_management/stop_order_strategies.html) — stop-loss, stop-limit, and trailing-stop orders
- [Kelly Criterion — Formula & Examples](risk_management/kelly_criterion.html) — edge-based position sizing
- [Risk-Adjusted Return Ratios](risk_management/risk_adjusted_return_ratios.html) — Sharpe, Sortino, Omega, Calmar, Martin
