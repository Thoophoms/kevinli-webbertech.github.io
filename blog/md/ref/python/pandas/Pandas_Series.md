# Pandas Series

Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). The axis labels are collectively called index.

## pandas.Series

A pandas Series can be created using the following constructor-

``` sh
pandas.Series(data, index, dtype, copy)
```

The parameters of the constructor are as follows:

1. **data** - data takes various forms like ndarray, list, constants
2. **index** - Index values must be unique and hashable, same length as data. Default **np.arrange(n)** if no index is passed.
3. **dtype** - dtype is for data type. If None, data type will be inferred.
4. **copy** - Copy data. Default False.

A series can be created using various inputs like -

* Array
* Dict
* Scalar value or constant

## Create an Empty Series

A basic series, which can be created is an Empty Series.

You can create an empty Series using `pd.Series()`.

```python
import pandas as pd
s = pd.Series()
print(s)
```
Output:
```
Series([], dtype: float64)
```

### Creating a Series from ndarray
If data is an ndarray, the index must be the same length as the data. If no index is provided, it defaults to `range(n)`.

Example 1:
```python
import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)
```
Output:
```
0    a
1    b
2    c
3    d
dtype: object
```

Example 2:
```python
import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[100, 101, 102, 103])
print(s)
```
Output:
```
100    a
101    b
102    c
103    d
dtype: object
```

### Creating a Series from dict
A dictionary can be passed as input. If no index is specified, the dictionary keys are taken in sorted order to construct the index.

Example 1:
```python
import pandas as pd

data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s)
```
Output:
```
a    0.0
b    1.0
c    2.0
dtype: float64
```

Example 2:
```python
import pandas as pd

data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data, index=['b', 'c', 'd', 'a'])
print(s)
```
Output:
```
b    1.0
c    2.0
d    NaN
a    0.0
dtype: float64
```

### Creating a Series from Scalar
If data is a scalar value, an index must be provided. The value will be repeated to match the length of the index.

```python
import pandas as pd

s = pd.Series(5, index=[0, 1, 2, 3])
print(s)
```
Output:
```
0    5
1    5
2    5
3    5
dtype: int64
```

## Accessing Data from Series with Position
Data in the series can be accessed similar to that in an ndarray.

### Example 1: Retrieve the first element
```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s[0])
```
Output:
```
1
```

### Example 2: Retrieve the first three elements
```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s[:3])
```
Output:
```
a    1
b    2
c    3
dtype: int64
```

### Example 3: Retrieve the last three elements
```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s[-3:])
```
Output:
```
c    3
d    4
e    5
dtype: int64
```

## Retrieve Data Using Label (Index)
A Series is like a fixed-size dict in that you can get and set values by index label.

### Example 1: Retrieve a single element using index label
```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s['a'])
```
Output:
```
1
```

### Example 2: Retrieve multiple elements using a list of index label values
```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s[['a', 'c', 'd']])
```
Output:
```
a    1
c    3
d    4
dtype: int64
```

### Example 3: Handling a non-existent label
If a label is not contained, an exception is raised.

```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s['f'])
```
Output:
```
KeyError: 'f'
```
Note: To handle missing labels gracefully, you can use the `get` method which returns `None` or a specified default value if the label is not found:
```python
print(s.get('f', 'Label not found'))
```
Output:
```
Label not found
```



