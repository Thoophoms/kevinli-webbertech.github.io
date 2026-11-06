# Microsoft Office Excel - PivotTables and Tables

## What Is an Excel Table?

An Excel table is a structured range of data with built-in filtering, sorting, and automatic formatting.

Benefits of tables:

- easier sorting and filtering
- formulas fill down automatically
- chart ranges update more easily
- structured references make formulas clearer

## What Is a PivotTable?

A PivotTable summarizes large data sets without changing the original raw data.

Use it to answer questions such as:

- total sales by month
- quantity sold by region
- average score by class
- count of orders by product

![PivotTable layout overview](/blog/images/spreadsheet/pivot_table_layout.svg)

## Sample Data

| Region | Product | Month | Sales |
|---|---|---|---:|
| East | Laptop | Jan | 1200 |
| West | Laptop | Jan | 1400 |
| East | Mouse | Feb | 250 |
| West | Mouse | Feb | 300 |

## Convert Data to a Table

1. Select the data.
2. Press **Ctrl+T**.
3. Confirm that the table has headers.

Once data is in a table, Excel treats it as a structured data source.

## Create a PivotTable

1. Click any cell in the table.
2. Choose **Insert > PivotTable**.
3. Select where to place the PivotTable.
4. Drag fields into **Rows**, **Columns**, **Values**, and **Filters**.

## Example 1: Sales by Region

- Put `Region` in **Rows**
- Put `Sales` in **Values**

Result:

| Region | Sum of Sales |
|---|---:|
| East | 1450 |
| West | 1700 |

## Example 2: Sales by Region and Month

- Put `Region` in **Rows**
- Put `Month` in **Columns**
- Put `Sales` in **Values**

This lets you compare totals across two dimensions.

## Useful PivotTable Operations

- sort high to low
- filter one product only
- change `Sum` to `Average` or `Count`
- refresh the PivotTable when source data changes

## Refresh a PivotTable

If the source data changes:

1. Click inside the PivotTable.
2. Choose **Refresh**.

## Practice

1. Create a sales table with at least eight rows.
2. Convert it to an Excel table.
3. Build a PivotTable showing total sales by product.
4. Add month as a column field.
5. Filter to show only one region.

## Common Mistakes

- source data does not have headers
- blank rows interrupt the table range
- text values are stored instead of numbers
- user forgets to refresh after changing data

## References

- [Microsoft Support: Create a PivotTable](https://support.microsoft.com/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576)