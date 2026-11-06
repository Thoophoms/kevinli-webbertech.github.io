# Google Sheets

## What Is Google Sheets?

Google Sheets is Google's cloud-based spreadsheet tool. It runs in a web browser, saves automatically to Google Drive, and is designed for real-time collaboration.

It is useful when you need to:

- share a workbook with a team quickly
- edit from school, home, or mobile devices
- track changes automatically
- use formulas, charts, filters, and pivot tables without installing software

![Google Sheets collaboration overview](/blog/images/spreadsheet/google_sheets_workflow.svg)

## Key Features

| Feature | What it does |
|---|---|
| Auto save | Saves changes to Google Drive automatically |
| Share | Lets multiple users view, comment, or edit |
| Version history | Restores earlier versions of a spreadsheet |
| Comments | Supports feedback and team discussion |
| Forms integration | Collects survey or response data directly into a sheet |
| Charts and pivot tables | Summarizes and visualizes data |

## Getting Started

1. Go to [https://sheets.google.com](https://sheets.google.com).
2. Sign in with a Google account.
3. Click **Blank spreadsheet**.
4. Rename the file at the top-left corner.
5. Enter labels in row 1, then add data under the headings.

## Basic Interface

- **Menu bar**: File, Edit, View, Insert, Format, Data, Tools, Extensions, Help
- **Toolbar**: quick actions such as bold, borders, fill color, merge, chart, and filter
- **Formula bar**: displays the content or formula of the selected cell
- **Rows and columns**: the grid area where data is stored
- **Sheet tabs**: lets you switch between worksheets in the same workbook

## Example: Classroom Grade Sheet

Create a table like this:

| Student | Quiz 1 | Quiz 2 | Homework | Final |
|---|---:|---:|---:|---:|
| Ana | 85 | 92 | 100 | 90 |
| Ben | 78 | 80 | 95 | 88 |
| Chris | 93 | 90 | 98 | 94 |

Useful formulas:

```excel
=AVERAGE(B2:E2)
=MAX(B2:E2)
=MIN(B2:E2)
```

If you want a letter grade:

```excel
=IF(AVERAGE(B2:E2)>=90,"A",IF(AVERAGE(B2:E2)>=80,"B","C"))
```

## Sharing and Permissions

Click **Share** in the top-right corner.

You can give users one of these permissions:

- **Viewer**: can read only
- **Commenter**: can add comments, but cannot edit cells
- **Editor**: can change the spreadsheet

This is one of the biggest advantages of Google Sheets compared with a local-only spreadsheet file.

## Useful Tools

### Filter

Use **Data > Create a filter** to show only the rows you want.

Example:

- show only students with Final score below 90
- sort names from A to Z
- sort scores from highest to lowest

### Conditional Formatting

Use **Format > Conditional formatting**.

Example:

- cells below 80 become red
- cells 90 and above become green

### Chart

1. Select your table.
2. Click **Insert > Chart**.
3. Pick a chart type such as column, line, or pie chart.

### Freeze Row

Use **View > Freeze > 1 row** so the heading row stays visible when you scroll.

## Version History

Google Sheets automatically stores changes.

Use **File > Version history > See version history** to:

- see who made changes
- restore an older version
- rename important versions such as `Week 1 Draft`

## Practical Example: Expense Tracker

| Date | Category | Description | Amount |
|---|---|---|---:|
| 2026-04-01 | Food | Lunch | 12.50 |
| 2026-04-02 | Transport | Bus card | 25.00 |
| 2026-04-03 | Books | Spreadsheet text | 48.00 |

Total expenses:

```excel
=SUM(D2:D4)
```

Average expense:

```excel
=AVERAGE(D2:D4)
```

## Tips

- Use short, clear column names
- Freeze the header row for larger sheets
- Protect important formulas with sheet protection
- Keep raw data on one sheet and summaries on another
- Use comments instead of changing someone else's work without explanation

## Practice

1. Create a weekly budget sheet with Income, Food, Transport, and Savings columns.
2. Add five rows of sample data.
3. Calculate total spending with `SUM`.
4. Apply a filter to show only one category.
5. Insert a chart based on the totals.

## References

- [Google Sheets Help Center](https://support.google.com/docs/topic/9054603)
- [Google Sheets Function List](https://support.google.com/docs/table/25273)
- [Google Workspace Learning Center](https://workspace.google.com/learning-center/products/sheets/)