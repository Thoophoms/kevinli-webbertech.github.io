# Class 9 - Backtesting & Strategy Building

## Goal

Build a simple, rules-based trading strategy and validate it against historical data.

## Topics

- Defining clear entry and exit rules
- Backtesting manually on historical charts
- Backtesting with spreadsheet or software tools
- Metrics to evaluate: win rate, average win/loss, max drawdown
- Avoiding overfitting a strategy to past data

## Definitions

- **Entry rule**: A specific, objective condition that must be met before opening a trade.
- **Exit rule**: A specific, objective condition (profit target, stop-loss, or signal) that determines when a trade is closed.
- **Backtesting**: Testing a trading strategy's rules against historical price data to evaluate how it would have performed.
- **Win rate**: The percentage of trades in a strategy or track record that were profitable.
- **Average win/loss**: The average profit of winning trades compared to the average loss of losing trades, used alongside win rate to judge profitability.
- **Max drawdown**: The largest peak-to-trough decline in a strategy's equity curve during the backtest or live trading period.
- **Overfitting**: Tuning a strategy's rules so closely to historical data that it loses predictive power on new, unseen data.

## Key Takeaways

- A strategy must have objective, repeatable rules to be backtestable.
- Win rate alone doesn't determine profitability; risk/reward matters just as much.
- Past performance does not guarantee future results, but backtesting builds confidence in the process.

## Practice

Define a simple moving-average crossover strategy and manually backtest it over the last 20 candles of a chart.
