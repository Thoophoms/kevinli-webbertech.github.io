# Pandas Aggregation

Once the rolling, expanding and ewm objects are created, several methods are available to perform aggregations on data.

### Apply Aggregation on a Whole DataFrame

```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Apply aggregation on the whole DataFrame
result = df.agg(['sum', 'mean'])
print(result)
```

### Apply Aggregation on a Single Column of a DataFrame

```python
# Apply aggregation on a single column
result_col = df['A'].agg(['sum', 'mean'])
print(result_col)
```

### Apply Aggregation on Multiple Columns of a DataFrame

```python
# Apply aggregation on multiple columns
result_multi_col = df.agg({'A': 'sum', 'B': 'mean'})
print(result_multi_col)
```

### Apply Multiple Functions on a Single Column of a DataFrame

```python
# Apply multiple functions on a single column
result_multiple_func_col = df['A'].agg(['sum', 'mean'])
print(result_multiple_func_col)
```

### Apply Multiple Functions on Multiple Columns of a DataFrame

```python
# Apply multiple functions on multiple columns
result_multiple_func_multi_col = df.agg({'A': ['sum', 'mean'], 'B': ['min', 'max']})
print(result_multiple_func_multi_col)
```

### Apply Different Functions to Different Columns of a DataFrame

```python
# Apply different functions to different columns
result_diff_func_diff_col = df.agg({'A': 'sum', 'B': lambda x: x.max() - x.min()})
print(result_diff_func_diff_col)
```

These examples demonstrate how to apply various aggregation functions on DataFrame objects in Pandas, allowing for flexible and powerful data analysis capabilities.