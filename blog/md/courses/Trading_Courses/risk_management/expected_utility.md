# Expected Utility

## What Is Expected Utility?

Expected utility is a decision-theory concept describing how a rational person is assumed to choose among
risky options: not by maximizing the expected (average) *dollar* outcome, but by maximizing the expected
value of a **utility function** — a mapping from wealth or outcomes to subjective "satisfaction." Because
that utility function is typically **concave** (each additional dollar matters a little less than the
last), expected-utility maximizers are usually risk-averse: they will often prefer a smaller certain gain
over a larger, riskier gamble with the same (or even higher) expected dollar value.

This distinction — maximizing expected utility rather than expected value — is the formal explanation for
why rational investors and traders routinely turn down bets and position sizes that have positive expected
value on paper, if those bets also carry a meaningful chance of ruin or a large enough potential loss.

## How It Shapes Decision-Making

Expected utility theory predicts and explains several everyday financial behaviors:

* **Buying insurance:** Paying a premium that exceeds the expected payout has *negative* expected value,
  yet it can still *increase* expected utility for a risk-averse person, because losing an uninsured asset
  reduces utility by more than the premium reduces it.
* **Diversification:** Spreading capital across uncorrelated positions lowers the variance of outcomes
  without necessarily lowering expected value — which raises expected utility for anyone with a concave
  utility function.
* **Position sizing below "full Kelly":** The full [Kelly Criterion](kelly_criterion.html) bet size
  maximizes long-run expected *growth rate* of wealth (itself a logarithmic-utility result — see below),
  but many traders size down further because their personal utility function penalizes large drawdowns
  more heavily than a log-utility investor would.
* **Risk/reward thresholds:** Why a trader might skip a trade with a technically positive
  [risk/reward ratio](risk_reward_ratio.html) if the position size needed to make it worthwhile also
  risks an uncomfortable fraction of the account — the dollar edge is positive, but the utility-adjusted
  edge may not be.

## Origins and Evolution

* **1738 — Daniel Bernoulli** proposed using utility (he suggested a logarithmic function of wealth) rather
  than raw monetary value to resolve the **St. Petersburg Paradox** — a coin-flip game with infinite
  expected monetary value that almost no one would actually pay a large sum to play.
* **1944 — John von Neumann and Oskar Morgenstern** formalized expected utility theory axiomatically in
  *Theory of Games and Economic Behavior*, showing that if a decision-maker's preferences satisfy a small
  set of consistency axioms (completeness, transitivity, continuity, and independence), their choices under
  uncertainty can be represented as maximizing the expectation of *some* utility function — the
  "von Neumann–Morgenstern utility theorem."
* **Later critiques** — behavioral economists (notably Daniel Kahneman and Amos Tversky, with **Prospect
  Theory**, 1979) showed that real human choices often violate the independence axiom and other
  predictions of expected utility theory (e.g., people weight losses more heavily than equivalent gains,
  and misjudge small probabilities). Expected utility remains the standard *normative* model for how a
  rational agent "should" choose, even where it's an imperfect *descriptive* model of how people actually
  behave.

## Expected Utility vs. Marginal Utility

These two concepts are related but answer different questions:

| | Marginal Utility | Expected Utility |
|---|---|---|
| **Question answered** | How much *additional* satisfaction does one more unit of wealth/consumption provide, under certainty? | How should a decision be evaluated when outcomes are *uncertain*? |
| **Core idea** | Diminishing marginal utility — each extra dollar is worth a little less than the one before | Weight each possible outcome's utility by its probability, then sum (or integrate) |
| **Typical use** | Explaining consumption/pricing decisions under certainty | Explaining choices among bets, insurance, investments, and position sizes |
| **Relationship** | Diminishing marginal utility is *why* utility functions are concave, which is *why* expected-utility maximizers are risk-averse | Expected utility is built from (and inherits the shape of) the underlying marginal-utility/utility function |

In short: **diminishing marginal utility is the ingredient; expected utility is the recipe** that uses that
ingredient to evaluate choices that involve risk.

## Examples of Expected Utility in Action

**Example 1 — Insurance:** A trader has a $2,000 piece of equipment with a 1% chance per year of being
destroyed (expected loss = $20/year). An insurer offers a policy for $35/year. In raw expected-value terms,
buying it is a losing bet (−$15/year expected). But under a concave utility function, the guaranteed small
loss (the premium) can produce higher expected utility than the small-probability, large-magnitude loss of
going uninsured — which is why insurance markets exist at all.

**Example 2 — Bet sizing:** Two traders are offered the same coin-flip-style edge from
[Kelly Criterion Example 1](kelly_criterion.html#example-1--coin-flip-classic) (60% win rate, 1:1 payoff,
full Kelly = 20% of bankroll per flip). A trader with a standard (log) utility function is comfortable at
or near the full-Kelly 20%. A more risk-averse trader — whose utility function penalizes large drawdowns
more sharply — maximizes *their own* expected utility at a smaller size, such as half- or quarter-Kelly,
even though 20% is "optimal" in the pure growth-rate sense.

**Example 3 — Two bets, same expected value:** Bet A pays $100 with certainty. Bet B pays $1,000 with a 10%
chance (and $0 otherwise) — identical $100 expected value. Most people strictly prefer Bet A. Expected
*value* alone cannot explain this common preference; expected *utility*, with a concave utility function,
can — the marginal utility of the first $100 is worth more than the marginal utility of the next $900 that
Bet B might, but probably won't, pay out.

## The Bottom Line

Expected utility theory is the formal reason "maximize expected value" is not the same thing as "make the
best decision" whenever risk and ruin are on the table. It underpins why risk-averse position sizing
(fractional [Kelly Criterion](kelly_criterion.html), fixed-percent
[position sizing](position_sizing.html), diversification, and
insurance) can be rational even when it leaves some expected dollars on the table — and it's a useful
mental model for understanding *why* a technically positive-edge trade or bet size can still be the wrong
one for a given trader's actual tolerance for loss.

### See Also

* [Kelly Criterion — Formula & Examples](kelly_criterion.html)
* [Risk/Reward Ratio: Day Trading vs. Swing Trading](risk_reward_ratio.html)
* [Risk-Adjusted Return Ratios](risk_adjusted_return_ratios.html)
* [Risk Management Deep Dive Hub](index.html)

### Ref

- [What Is Expected Utility?](https://www.investopedia.com/terms/e/expectedutility.asp#toc-what-is-expected-utility)
- [How It Shapes Decision-Making](https://www.investopedia.com/terms/e/expectedutility.asp#toc-how-expected-utility-shapes-decision-making)
- [Origins and Evolution](https://www.investopedia.com/terms/e/expectedutility.asp#toc-the-origins-and-evolution-of-expected-utility)
- [Expected Utility vs. Marginal Utility](https://www.investopedia.com/terms/e/expectedutility.asp#toc-comparing-expected-utility-and-marginal-utility)
- [Examples](https://www.investopedia.com/terms/e/expectedutility.asp#toc-examples-of-expected-utility-in-action)
- [The Bottom Line](https://www.investopedia.com/terms/e/expectedutility.asp#toc-the-bottom-line)
