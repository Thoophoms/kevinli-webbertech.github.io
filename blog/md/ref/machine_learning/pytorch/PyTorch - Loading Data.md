# PyTorch - Loading Data

PyTorch includes a package called `torchvision` which is used to load and prepare datasets. It provides two essential classes for dataset handling: `Dataset` and `DataLoader`. These classes help in transforming and loading datasets efficiently.

## Dataset

The `Dataset` class is used to represent and access the data in your dataset

# Load the CIFAR-10 training dataset
trainset = torchvision.datasets.CIFAR10(
    root='./data',        # Directory where the dataset will be stored
    train=True,           # Load the training set
    download=True,        # Download the dataset if not already present
    transform=transform  # Transform to apply to each image
)

## Example: Loading CSV File

We use the Python package `pandas` to load the CSV file. The original file has the following format: (image name, 68 landmarks - each landmark has x, y coordinates).

```python
import pandas as pd

# Load the CSV file
landmarks_frame = pd.read_csv('faces/face_landmarks.csv')

# Access a specific entry
n = 65
img_name = landmarks_frame.iloc[n, 0]
landmarks = landmarks_frame.iloc[n, 1:].values  # Use .values instead of .as_matrix()
landmarks = landmarks.astype('float').reshape(-1, 2)
```
