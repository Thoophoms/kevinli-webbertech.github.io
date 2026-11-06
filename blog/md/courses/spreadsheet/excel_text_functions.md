# Microsoft Office Excel - Advanced Text Functions

## Why Text Functions Matter

Text functions help clean, standardize, and combine data.

They are useful when:

- names are written in inconsistent case
- extra spaces break comparisons
- first and last names must be combined
- codes must be extracted from larger text strings

![Text function examples](/blog/images/spreadsheet/text_function.png)

## Common Text Functions

| Function | Purpose |
|---|---|
| `UPPER` | Converts text to uppercase |
| `LOWER` | Converts text to lowercase |
| `PROPER` | Converts text to title case |
| `TRIM` | Removes extra spaces |
| `LEFT` | Returns leftmost characters |
| `RIGHT` | Returns rightmost characters |
| `MID` | Returns characters from the middle |
| `TEXTJOIN` or `CONCAT` | Combines text |

## Basic Examples

If cell `A2` contains `john smith`:

```excel
=UPPER(A2)
=LOWER(A2)
=PROPER(A2)
```

Results:

- `JOHN SMITH`
- `john smith`
- `John Smith`

## TRIM Example

If cell `A3` contains `   Ana Lee   ` with extra spaces:

```excel
=TRIM(A3)
```

This removes leading and trailing spaces.

![TRIM function example](/blog/images/spreadsheet/trim_function.png)

## LEFT, RIGHT, and MID

Suppose `B2` contains `IT-2026-001`.

```excel
=LEFT(B2,2)
=RIGHT(B2,3)
=MID(B2,4,4)
```

Results:

- `IT`
- `001`
- `2026`

## Combining Text

If `C2` contains first name and `D2` contains last name:

```excel
=C2&" "&D2
```

Or:

```excel
=CONCAT(C2," ",D2)
```

## Example: Create Email Addresses

If first name is in `A2` and last name is in `B2`:

```excel
=LOWER(A2&"."&B2&"@school.edu")
```

## Example: Extract Department Code

If `A2` contains `CS-DEV-101`:

```excel
=LEFT(A2,2)
```

If you want the middle section:

```excel
=MID(A2,4,3)
```

## Practice Table

| Raw Name | Clean Name |
|---|---|
| `   kevin LI   ` | `=PROPER(TRIM(A2))` |
| `JANE DOE` | `=PROPER(A3)` |

## Practice

1. Enter five messy names.
2. Use `TRIM`, `LOWER`, `UPPER`, and `PROPER` to clean them.
3. Build a full email address from first and last names.
4. Extract the first two letters of a code with `LEFT`.

## References

- [Microsoft Support: Text Functions](https://support.microsoft.com/office/text-functions-reference-cccd86ad-547d-4ea9-a065-7bb697c2a56e)