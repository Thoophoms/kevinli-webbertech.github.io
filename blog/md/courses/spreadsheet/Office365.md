# Microsoft 365 and Excel for the Web

## What Is Microsoft 365?

Microsoft 365 is Microsoft's cloud productivity platform. It includes applications such as Word, Excel, PowerPoint, Outlook, OneDrive, and Teams.

For spreadsheet work, Microsoft 365 gives you:

- **Excel desktop** for advanced features
- **Excel for the web** for browser-based editing
- **OneDrive** for cloud storage and file sharing
- **co-authoring** so multiple people can edit one workbook

![Microsoft 365 spreadsheet workflow](/blog/images/spreadsheet/office365_cloud_flow.svg)

## Common Versions of Excel

| Version | Best use |
|---|---|
| Excel desktop | Advanced formulas, Power Query, Power Pivot, large workbooks |
| Excel for the web | Quick edits, collaboration, sharing, school and office use |
| Excel mobile | Small updates on phones and tablets |

## Main Benefits of Microsoft 365

- Files are saved in the cloud through OneDrive
- You can share a workbook with a link
- Changes are saved automatically
- Teams can collaborate on the same workbook
- Comments and mentions help with communication

## Creating a Workbook in OneDrive

1. Go to [https://www.office.com](https://www.office.com).
2. Sign in with a Microsoft 365 account.
3. Open **Excel**.
4. Choose **Blank workbook**.
5. Rename the file.

## Excel for the Web Interface

- **Ribbon**: Home, Insert, Formulas, Data, Review, View
- **Name box**: shows the active cell reference
- **Formula bar**: enter or edit formulas
- **Worksheet grid**: cells for data entry
- **Sheet tabs**: switch between worksheets
- **Share button**: invites collaborators

## Example: Sales Tracker

| Product | Units | Unit Price | Revenue |
|---|---:|---:|---:|
| Keyboard | 12 | 25 | 300 |
| Mouse | 20 | 18 | 360 |
| Monitor | 5 | 170 | 850 |

Revenue formula for row 2:

```excel
=B2*C2
```

Total revenue:

```excel
=SUM(D2:D4)
```

Average units sold:

```excel
=AVERAGE(B2:B4)
```

## Sharing a Workbook

1. Click **Share**.
2. Enter an email address or copy a sharing link.
3. Choose whether the person can **view** or **edit**.
4. Send the link.

This makes Microsoft 365 useful for group assignments, office reports, and class projects.

## Co-Authoring

When several users open the same workbook from OneDrive or SharePoint:

- everyone can edit at the same time
- colored indicators show who is active
- comments can be added to specific cells
- changes are saved automatically

## Useful Cloud Features

### AutoSave

If the workbook is stored in OneDrive, changes save automatically.

### Comments

Use comments to explain:

- why a formula changed
- what data needs review
- who should verify a section

### Version History

You can restore an earlier version if a mistake was made.

## Differences: Excel Desktop vs Excel Web

| Feature | Desktop | Web |
|---|---|---|
| Basic formulas | Yes | Yes |
| Charts | Yes | Yes |
| Sharing | Yes | Yes |
| AutoSave | Yes, with OneDrive | Yes |
| Power Query | Stronger support | Limited |
| Large complex workbooks | Better | More limited |

## Practical Example: Shared Project Budget

| Item | Budget | Actual | Difference |
|---|---:|---:|---:|
| Software | 500 | 450 | -50 |
| Hardware | 1200 | 1325 | 125 |
| Training | 300 | 260 | -40 |

Difference formula:

```excel
=C2-B2
```

You can then use conditional formatting:

- red for positive difference values above budget
- green for negative values under budget

## Tips

- Save workbooks to OneDrive instead of a local Downloads folder
- Name files clearly, for example `budget_spring_2026.xlsx`
- Use separate worksheets for raw data, summary, and charts
- Add comments before making major changes in shared files
- Use version history before deleting large sections of data

## Practice

1. Create a workbook named `TeamBudget`.
2. Add a table with Budget, Actual, and Difference.
3. Share it with a classmate.
4. Ask the classmate to update one row.
5. Review the change in version history.

## References

- [Microsoft Excel Training](https://support.microsoft.com/excel)
- [Microsoft 365 Training Center](https://support.microsoft.com/training)
- [Excel for the Web Help](https://support.microsoft.com/office/excel-for-the-web-help-9a38efef-8f94-46f1-91c6-8e8fd96b6e35)