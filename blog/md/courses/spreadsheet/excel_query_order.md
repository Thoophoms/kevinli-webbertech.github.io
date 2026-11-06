# Microsoft Office Excel - Sorting, Filtering, and Querying Data

## Why Query and Order Data?

As spreadsheets grow, you need tools to find information quickly.

Three essential operations are:

- **sorting**: putting data in ascending or descending order
- **filtering**: showing only records that match conditions
- **querying**: extracting or analyzing specific parts of a data set

![Sort and filter workflow](/blog/images/spreadsheet/sort_filter_query.svg)

## Sample Data

| ID | Name | Department | Salary |
|---|---|---|---:|
| 101 | Ana | IT | 65000 |
| 102 | Ben | HR | 52000 |
| 103 | Chris | IT | 70000 |
| 104 | Dana | Sales | 61000 |

## Sorting Data

### Sort Names A to Z

1. Select the table.
2. Go to **Data**.
3. Choose **Sort A to Z** on the `Name` column.

### Sort Salary Highest to Lowest

Use **Sort Largest to Smallest** on the `Salary` column.

This is helpful for ranking results.

## Filtering Data

1. Select the header row.
2. Go to **Data > Filter**.
3. Click the dropdown arrow on a column.

Examples:

- show only department = `IT`
- show only salary greater than 60000
- show only names starting with `A`

## Using `SORT` and `FILTER` Functions

In newer versions of Excel and Google Sheets, dynamic array functions can help.

### Sort Example

```excel
=SORT(A2:D5,4,-1)
```

This sorts the range by the 4th column in descending order.

### Filter Example

```excel
=FILTER(A2:D5,C2:C5="IT")
```

This returns only rows where the department is IT.

## Lookup Example

If you want the salary for employee 103:

```excel
=XLOOKUP(103,A2:A5,D2:D5)
```

Older Excel versions may use `VLOOKUP` instead.

## Practical Example: Student List

| Student | Major | GPA |
|---|---|---:|
| Alice | CS | 3.8 |
| Brian | Math | 3.2 |
| Chloe | CS | 3.9 |
| David | History | 3.1 |

Questions you can answer quickly:

- who has the highest GPA?
- which students are in CS?
- which students have GPA above 3.5?

## Practice

1. Create a table with five employees.
2. Sort by salary from highest to lowest.
3. Filter to show only one department.
4. Use `FILTER` or `XLOOKUP` to return a smaller result set.

## Tips

- keep one clean header row
- do not merge cells inside the data table
- use consistent data types in each column
- convert large ranges into tables for easier filtering

## References

- [Microsoft Support: Sort Data in a Range or Table](https://support.microsoft.com/office/sort-data-in-a-range-or-table-c5f3e0d6-8c8d-4a39-b3ef-0f5f49b6b220)
- [Microsoft Support: Filter Data in a Range or Table](https://support.microsoft.com/office/filter-data-in-a-range-or-table-01832226-31b5-4568-8806-38c37dcc180e)