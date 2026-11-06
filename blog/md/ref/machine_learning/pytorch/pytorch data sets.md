# Dataset Loaders in PyTorch


PyTorch includes the following dataset loaders:

- **MNIST**
- **COCO (Captioning and Detection)**


Dataset includes majority of two types of functions given below −

Dataset includes the majority of two types of functions given below:

- **Transform**: A function that takes in an image and returns a modified version of standard stuff. These can be composed together with other transforms.


- **Target_transform**: A function that takes the target and transforms it. For example, it takes in a caption string and returns a tensor of word indices.



# MNIST Dataset

The following is a sample code for loading the MNIST dataset:

```python
dset.MNIST(root, train=True, transform=None, target_transform=None, download=False)
```
The parameters are as follows:

- **root**: The root directory of the dataset where the processed data exists.
- **train**: 
  - `True`: Loads the training set
  - `False`: Loads the test set
- **download**: 
  - `True`: Downloads the dataset from the internet and stores it in the root directory
  - `False`: Does not download the dataset and expects it to be available in the root directory


# COCO Dataset

To use the COCO dataset with PyTorch, you need to have the COCO API installed. Below is an example demonstrating how to load and use the COCO dataset with PyTorch:

```python
import torchvision.datasets as dset
import torchvision.transforms as transforms

# Initialize the COCO Captions dataset
cap = dset.CocoCaptions(
    root='dir where images are',
    annFile='json annotation file',
    transform=transforms.ToTensor()
)

# Print the number of samples in the dataset
print('Number of samples:', len(cap))
print(target)
```
The output achieved is as follows:

- **Number of samples**: 82,783
- **Image Size**: (3, 427, 640)


