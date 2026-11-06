# Pandas DataFrame

## Introduction to Pandas DataFrame
A Pandas DataFrame is a two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns). It is similar to a spreadsheet or SQL table.

## Importing Pandas
``` sh
import pandas as pd
```

## Creating a DataFrame

### From a Dictionary
```sh
data = {
    'column1': [1, 2, 3, 4],
    'column2': ['a', 'b', 'c', 'd']
}
df = pd.DataFrame(data)
```

### From a List of Dictionaries
```sh
data = [
    {'column1': 1, 'column2': 'a'},
    {'column1': 2, 'column2': 'b'},
    {'column1': 3, 'column2': 'c'},
    {'column1': 4, 'column2': 'd'}
]
df = pd.DataFrame(data)
```

### From a List of Lists
```sh
data = [
    [1, 'a'],
    [2, 'b'],
    [3, 'c'],
    [4, 'd']
]
df = pd.DataFrame(data, columns=['column1', 'column2'])
```

### From a Numpy Array
```sh
import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(data, columns=['a', 'b', 'c'])
```

### From another DataFrame
```sh
df_copy = df.copy()
```

## DataFrame Attributes
- **`index`**: Row labels.
- **`columns`**: Column labels.
- **`dtypes`**: Data types of each column.
- **`shape`**: Dimensions of the DataFrame (rows, columns).

## Accessing Data

### Selecting Columns
```python
df['column1']  # Selects a single column, returns a Series.
df[['column1', 'column2']]  # Selects multiple columns, returns a DataFrame.
```

### Selecting Rows
#### Using `.loc`
- **Definition**: `.loc` is label-based indexing, which means you have to specify the name of the rows and columns you want to filter.
```python
df.loc[0]  # Selects the first row by label.
df.loc[0:2]  # Selects rows from index 0 to 2 (inclusive).
df.loc[0:2, 'column1':'column2']  # Selects rows 0 to 2 and columns 'column1' to 'column2'.
```

#### Using `.iloc`
- **Definition**: `.iloc` is integer-location based indexing, which means you have to specify the index of the rows and columns you want to filter.
```python
df.iloc[0]  # Selects the first row by position.
df.iloc[0:2]  # Selects rows from position 0 to 2 (exclusive).
df.iloc[0:2, 0:2]  # Selects rows 0 to 2 and columns 0 to 2.
```

## Adding/Removing Data

### Adding Columns
```python
df['new_column'] = [5, 6, 7, 8]  # Adds a new column to the DataFrame.
```

### Dropping Columns
```python
df.drop('column1', axis=1, inplace=True)  # Drops a column. axis=1 indicates column-wise operation. inplace=True modifies the DataFrame in place.
```

### Adding Rows
```python
new_row = {'column1': 5, 'column2': 'e'}
df = df.append(new_row, ignore_index=True)  # Adds a new row to the DataFrame. ignore_index=True resets the index.
```

### Dropping Rows
```python
df.drop(0, axis=0, inplace=True)  # Drops a row. axis=0 indicates row-wise operation. inplace=True modifies the DataFrame in place.
```

## Handling Missing Data

### Detecting Missing Data
```python
df.isnull()  # Returns a DataFrame of the same shape with boolean values indicating missing data.
df.notnull()  # Returns a DataFrame of the same shape with boolean values indicating non-missing data.
```

### Filling Missing Data
```python
df.fillna(0, inplace=True)  # Replaces all NaN values with 0. inplace=True modifies the DataFrame in place.
```

### Dropping Missing Data
```python
df.dropna(axis=0, inplace=True)  # Drops rows with any missing values. axis=0 indicates row-wise operation. inplace=True modifies the DataFrame in place.
df.dropna(axis=1, inplace=True)  # Drops columns with any missing values. axis=1 indicates column-wise operation. inplace=True modifies the DataFrame in place.
```

## DataFrame Operations

### Basic Operations
```python
df['column1'] + df['column2']  # Adds values of 'column1' and 'column2'.
df['column1'] * 2  # Multiplies values of 'column1' by 2.
```

### Applying Functions
#### Using `apply`
- **Definition**: Applies a function along an axis of the DataFrame.
```python
df.apply(np.sqrt)  # Applies NumPy's square root function to each element.
```

#### Using `applymap`
- **Definition**: Applies a function to each element of the DataFrame.
```python
df.applymap(lambda x: x*2)  # Multiplies each element by 2.
```

## Grouping Data
- **Definition**: Used for aggregating data by splitting it into groups based on some criteria.
```python
df.groupby('column1').sum()  # Groups the data by 'column1' and calculates the sum of each group.
df.groupby(['column1', 'column2']).mean()  # Groups the data by 'column1' and 'column2' and calculates the mean of each group.
```

## Merging DataFrames

### Concatenating
- **Definition**: Concatenates DataFrames along a particular axis.
```python
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']})

df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'],
                    'B': ['B3', 'B4', 'B5']})

result = pd.concat([df1, df2])  # Concatenates df1 and df2 along the rows.
```

### Merging
- **Definition**: Merges DataFrames using a database-style join.
```python
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value': [1, 2, 3, 4]})

df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
                    'value': [5, 6, 7, 8]})

result = pd.merge(df1, df2, on='key', how='inner')  # Merges df1 and df2 on 'key' using an inner join.
```

## Sorting and Ranking

### Sorting
```python
df.sort_values(by='column1', ascending=False)  # Sorts the DataFrame by 'column1' in descending order.
df.sort_index(axis=1, ascending=False)  # Sorts the DataFrame by column labels in descending order.
```

### Ranking
```python
df['rank'] = df['column1'].rank()  # Assigns ranks to the values in 'column1'.
```

## Statistical Operations
```python
df.describe()  # Generates descriptive statistics.
df.mean()  # Calculates the mean of each column.
df.corr()  # Calculates the correlation matrix.
df.count()  # Counts the number of non-NA/null entries.
df.max()  # Finds the maximum value in each column.
df.min()  # Finds the minimum value in each column.
df.median()  # Calculates the median of each column.
df.std()  # Calculates the standard deviation of each column.
```

## Handling Duplicates
```python
df.duplicated()  # Returns a Series indicating duplicate rows.
df.drop_duplicates(inplace=True)  # Removes duplicate rows. inplace=True modifies the DataFrame in place.
```

## String Operations
```python
df['column2'].str.lower()  # Converts all strings in 'column2' to lowercase.
df['column2'].str.contains('pattern')  # Checks if each string in 'column2' contains the substring 'pattern'.
```

## Date Functionality
```python
df['date'] = pd.to_datetime(df['date'])  # Converts the 'date' column to datetime.
df['year'] = df['date'].dt.year  # Extracts the year from the 'date' column.
df['month'] = df['date'].dt.month  # Extracts the month from the 'date' column.
df['day'] = df['date'].dt.day  # Extracts the day from the 'date' column.
```

## Plotting
```python
df.plot(kind='line')  # Plots a line graph.
df['column1'].plot(kind='hist')  # Plots a histogram

```markdown
df['column1'].plot(kind='hist')  # Plots a histogram for 'column1'.
```

## Saving and Loading Data

### To CSV
```python
df.to_csv('filename.csv', index=False)  # Saves the DataFrame to a CSV file. index=False prevents the index from being written.
```

### From CSV
```python
df = pd.read_csv('filename.csv')  # Reads a CSV file into a DataFrame.
```

### To Excel
```python
df.to_excel('filename.xlsx', index=False)  # Saves the DataFrame to an Excel file. index=False prevents the index from being written.
```

### From Excel
```python
df = pd.read_excel('filename.xlsx')  # Reads an Excel file into a DataFrame.
```

## Additional Notes
- **Versatility**: DataFrames support many operations similar to SQL or Excel, making them very versatile for data manipulation.
- **Integration**: Built on top of NumPy, ensuring high performance and compatibility with other data science libraries.
- **Data Sources**: Can easily handle various data sources and formats, making them ideal for data analysis tasks.

## Examples and Use Cases

### Example: Analyzing a DataFrame
Here's a practical example to demonstrate some common operations on a DataFrame:

```python
# Importing pandas
import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, 60000, 90000, 85000]
}
df = pd.DataFrame(data)

# Viewing the DataFrame
print(df)

# Descriptive Statistics
print(df.describe())

# Sorting the DataFrame by Age
df_sorted = df.sort_values(by='Age')
print(df_sorted)

# Filtering Data: Employees with Salary > 75000
high_salary_df = df[df['Salary'] > 75000]
print(high_salary_df)

# Adding a new column: Bonus
df['Bonus'] = df['Salary'] * 0.1
print(df)

# Handling Missing Data: Filling NaN values
df_with_nan = df.copy()
df_with_nan.loc[2, 'Salary'] = None
print(df_with_nan)
df_with_nan_filled = df_with_nan.fillna(df_with_nan['Salary'].mean())
print(df_with_nan_filled)
```

### Example: Grouping and Aggregation
Using the same DataFrame, let's demonstrate grouping and aggregation:

```python
# Creating a new column 'Department'
df['Department'] = ['HR', 'Finance', 'IT', 'Finance', 'HR']

# Grouping by Department and calculating mean Salary
department_salary = df.groupby('Department')['Salary'].mean()
print(department_salary)

# Aggregating multiple functions: mean and sum of Salary
department_agg = df.groupby('Department')['Salary'].agg(['mean', 'sum'])
print(department_agg)
```

### Example: Merging DataFrames
Demonstrating how to merge two DataFrames:

```python
# Creating another DataFrame
data2 = {
    'Department': ['HR', 'Finance', 'IT', 'Marketing'],
    'Budget': [100000, 150000, 120000, 130000]
}
df2 = pd.DataFrame(data2)

# Merging on 'Department'
merged_df = pd.merge(df, df2, on='Department', how='left')
print(merged_df)
```

These examples highlight the flexibility and power of Pandas DataFrames in data analysis and manipulation. By mastering these techniques, you can efficiently handle, analyze, and visualize complex datasets.

## Conclusion
Pandas DataFrame is an essential tool for data manipulation and analysis in Python. With its wide range of functionalities and ease of use, it is a powerful library that helps in managing and analyzing data efficiently. By understanding and utilizing the various methods and operations available in Pandas, you can perform a wide variety of data tasks with ease.

