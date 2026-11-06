# Black-Scholes Model

The Black-Scholes model (Black & Scholes, 1973; extended by Robert Merton the same year — all three later
shared/won recognition for this work, with Myron Scholes and Robert Merton receiving the 1997 Nobel
Memorial Prize in Economic Sciences, Fischer Black having died in 1995) is the foundational closed-form
formula for pricing European-style options. It's the pricing engine behind the option Greeks
(Delta, Gamma, Theta, Vega, Rho) used throughout options trading.

> **Disclaimer:** Black-Scholes prices *European* options (exercisable only at expiration) under a set of
> simplifying assumptions that don't perfectly hold in real markets (see Limitations below). Real option
> prices can and do diverge from the model, especially around earnings, low-liquidity strikes, and American-style
> early-exercise situations (e.g., dividend-paying stocks).

## The Formula

For a non-dividend-paying stock:

```
Call price:  C = S₀·N(d1) − K·e^(−rT)·N(d2)
Put price:   P = K·e^(−rT)·N(−d2) − S₀·N(−d1)

where:
d1 = [ln(S₀/K) + (r + σ²/2)·T] / (σ·√T)
d2 = d1 − σ·√T
```

| Symbol | Meaning |
|---|---|
| `S₀` | Current price of the underlying asset |
| `K` | Strike price of the option |
| `r` | Risk-free interest rate (annualized, continuously compounded) |
| `T` | Time to expiration, in years |
| `σ` | Volatility of the underlying's returns (annualized standard deviation) |
| `N(x)` | Cumulative distribution function of the standard normal distribution — the probability a standard normal variable is ≤ x |

`N(d2)` is often read as the (risk-neutral) probability the option expires in-the-money; `N(d1)` is the
hedge ratio (and equals the option's Delta for a call).

## Key Assumptions

* The underlying's returns follow a **lognormal distribution** with constant volatility `σ` (no volatility
  changes, no jumps/gaps).
* **Constant, known risk-free rate** `r` over the option's life.
* **No dividends** during the option's life (the base formula above; dividend-adjusted variants exist).
* **European exercise only** — the option can only be exercised at expiration, not before.
* **No transaction costs or taxes**, and the underlying can be freely bought/sold/shorted in any quantity.
* Markets are **arbitrage-free** and trading is continuous.

## Worked Example

Hypothetical inputs (illustrative only, not live market data):

* `S₀ = $100` (current stock price)
* `K = $105` (strike price)
* `r = 4%` annual risk-free rate
* `T = 0.5` years (6 months to expiration)
* `σ = 30%` annualized volatility

```
d1 = [ln(100/105) + (0.04 + 0.30²/2) × 0.5] / (0.30 × √0.5)
   = [−0.0488 + 0.0425] / 0.2121
   = −0.0063 / 0.2121
   ≈ −0.0297

d2 = d1 − σ√T = −0.0297 − 0.2121 ≈ −0.2418

N(d1) ≈ 0.4882     N(d2) ≈ 0.4045
N(−d1) ≈ 0.5118    N(−d2) ≈ 0.5955

Call price = 100 × 0.4882 − 105 × e^(−0.04×0.5) × 0.4045
           ≈ 48.82 − 105 × 0.9802 × 0.4045
           ≈ 48.82 − 41.63
           ≈ $7.19

Put price  = 105 × e^(−0.04×0.5) × 0.5955 − 100 × 0.5118
           ≈ 102.92 × 0.5955 − 51.18
           ≈ 61.29 − 51.18
           ≈ $10.11
```

**Sanity check (put-call parity):** `C − P` should equal `S₀ − K·e^(−rT)`. Here, `7.19 − 10.11 ≈ −2.92`,
and `100 − 105×0.9802 ≈ 100 − 102.92 ≈ −2.92` — they match, confirming internal consistency.

## Relationship to the Option Greeks

Each Greek is a partial derivative of the Black-Scholes price with respect to one input, holding the others
constant — e.g., **Delta** (`∂C/∂S₀`) ≈ `N(d1)` for a call, **Vega** (`∂C/∂σ`) measures sensitivity to
volatility, and **Theta** (`∂C/∂T`, sign-flipped) measures time decay.

## Why It Matters for Risk Management

* **Implied volatility:** In practice, traders invert the formula — plugging in the *observed market price*
  of an option and solving for the `σ` that reproduces it. That implied volatility, not a historical/realized
  volatility number, is the market's forward-looking estimate of risk and is the figure most quoted for options.
* **Risk-neutral valuation:** Black-Scholes prices options as if all investors were risk-neutral (indifferent
  between a certain outcome and a risky one with the same expected value) — a simplifying assumption, not a
  claim about real investor psychology. Compare with [Expected Utility](expected_utility.html), which
  describes how *actual* risk-averse decision-makers evaluate uncertain outcomes.
* **Position sizing inputs:** Option Greeks derived from this model (Delta especially) feed directly into
  [position sizing](position_sizing.html) decisions for options trades.

## Limitations

* Assumes constant volatility, but real implied volatility varies by strike and expiration (the
  **volatility smile/skew**) — a well-known deviation from the model's own assumptions.
* Doesn't handle **early exercise** (American options), which matters for dividend-paying stocks and some
  index/futures options; practitioners use binomial trees or other numerical models for those cases.
* Assumes continuous, frictionless trading — real markets have bid/ask spreads, position limits, and
  liquidity gaps the model ignores.
* Tail risk (large jumps, gaps, "black swan" moves) is understated because returns are assumed lognormal,
  not fat-tailed.

### See Also

* [Kelly Criterion — Formula & Examples](kelly_criterion.html)
* [Expected Utility](expected_utility.html)
* [Risk-Adjusted Return Ratios](risk_adjusted_return_ratios.html)
* [Risk Management Deep Dive Hub](index.html)

### Ref

- [Black-Scholes Model — Investopedia](https://www.investopedia.com/terms/b/blackscholes.asp)
- [The Original 1973 Paper (Black & Scholes, JPE)](https://www.cs.princeton.edu/courses/archive/fall09/cos323/papers/black_scholes73.pdf)
