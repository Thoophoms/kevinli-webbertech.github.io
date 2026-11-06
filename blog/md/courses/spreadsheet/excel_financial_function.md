# Microsoft Office Excel - Financial Functions

## What Are Financial Functions?

Financial functions help calculate payments, present value, future value, interest, and investment performance.

They are commonly used for:

- loans
- mortgages
- savings plans
- business forecasts
- investment analysis

![Financial planning timeline](/blog/images/spreadsheet/financial_functions_timeline.svg)

## Common Financial Functions

| Function | Purpose |
|---|---|
| `PMT` | Calculates a periodic loan payment |
| `FV` | Finds future value of an investment |
| `PV` | Finds present value |
| `RATE` | Finds interest rate per period |
| `NPV` | Net present value |

## PMT Example: Monthly Loan Payment

Suppose:

- loan amount = 10000
- annual interest rate = 6%
- loan term = 3 years

Monthly payment formula:

```excel
=PMT(6%/12,3*12,-10000)
```

Explanation:

- `6%/12` = monthly interest rate
- `3*12` = 36 monthly payments
- `-10000` = present loan amount

## FV Example: Savings Growth

Suppose you deposit 200 each month for 5 years at 4% annual interest.

```excel
=FV(4%/12,5*12,-200,0)
```

This estimates how much money will accumulate in the future.

## PV Example: Current Value of Future Money

If you expect to receive 5000 in three years and the discount rate is 5%:

```excel
=PV(5%,3,0,5000)
```

## NPV Example

Cash flows:

| Year | Cash Flow |
|---|---:|
| 0 | -5000 |
| 1 | 1800 |
| 2 | 2200 |
| 3 | 2500 |

Formula:

```excel
=NPV(8%,B3:B5)+B2
```

This tells you whether the project returns enough value after accounting for discount rate.

## Important Sign Convention

In financial formulas:

- money paid out is usually negative
- money received is usually positive

If signs are wrong, the answer may appear with the wrong direction.

## Practical Example: Car Loan

| Item | Value |
|---|---:|
| Loan | 18000 |
| Annual Rate | 5.5% |
| Years | 4 |

Monthly payment:

```excel
=PMT(5.5%/12,4*12,-18000)
```

## Practice

1. Use `PMT` to calculate payment on a 25000 loan over 5 years at 7%.
2. Use `FV` to estimate savings if you invest 150 monthly for 10 years at 6%.
3. Create a cash-flow table and calculate `NPV`.

## Tips

- Always check whether rates are annual or monthly
- Match the number of periods to the rate period
- Use cell references instead of typing values directly into formulas
- Label assumptions clearly in the worksheet

## References

- [Microsoft Support: Financial Functions](https://support.microsoft.com/office/financial-functions-reference-5658ae39-b1f9-42f4-a0d9-0e3d1751c8f9)