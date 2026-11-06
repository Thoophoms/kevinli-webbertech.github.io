# Microsoft Office Excel - Multiple Worksheets

## Why Use Multiple Worksheets?

Multiple worksheets help you organize related data inside one workbook.

For example:

- one sheet for raw sales data
- one sheet for monthly summary
- one sheet for charts
- one sheet for assumptions or notes

![Workbook tabs and sheet references](/blog/images/spreadsheet/workbook_tabs.svg)

## Common Workbook Structure

| Sheet Name | Purpose |
|---|---|
| `RawData` | Original transactions or imported data |
| `Summary` | Totals, averages, KPIs |
| `Charts` | Visual reports |
| `Notes` | Explanations and assumptions |

## Renaming Worksheets

1. Double-click the sheet tab.
2. Type a meaningful name.
3. Press Enter.

Avoid names like `Sheet1`, `Sheet2`, and `Sheet3` when the workbook becomes larger.

## Add and Delete Worksheets

- Click the **plus** sign to add a new sheet
- Right-click a tab to rename, move, copy, or delete it

## Referencing Another Worksheet

If cell `B2` on sheet `Summary` should use a value from sheet `RawData`, use:

```excel
=RawData!B2
```

If the sheet name contains spaces:

```excel
='Monthly Sales'!B2
```

## Example: Sales Workbook

### Sheet 1: RawData

| Date | Product | Amount |
|---|---|---:|
| 2026-04-01 | Laptop | 900 |
| 2026-04-02 | Mouse | 25 |
| 2026-04-03 | Keyboard | 60 |

### Sheet 2: Summary

Total sales formula:

```excel
=SUM(RawData!C2:C4)
```

Average sale formula:

```excel
=AVERAGE(RawData!C2:C4)
```

## Move or Copy a Worksheet

Use this when you want to create a template for a new month.

1. Right-click the worksheet tab.
2. Choose **Move or Copy**.
3. Check **Create a copy** if needed.

## Color Coding Tabs

For large workbooks, assign colors to tabs:

- green for input sheets
- blue for reports
- red for confidential or locked sheets

## Practice

1. Create a workbook with three worksheets: `Expenses`, `Summary`, and `Charts`.
2. Enter sample data on `Expenses`.
3. Use formulas on `Summary` to total the expenses.
4. Insert a chart based on the summary values.

## Common Mistakes

- using unclear sheet names
- placing raw data and reports on the same crowded sheet
- deleting a sheet that is still referenced by formulas
- forgetting single quotes around sheet names with spaces

## References

- [Microsoft Support: Move or Copy Worksheets](https://support.microsoft.com/office/move-or-copy-worksheets-or-worksheet-data-3af35ecf-4b14-4e21-807c-3f3c4f9f3bfa)