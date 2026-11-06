# Face Detection Application

Real-world datasets are noisy and heterogeneous, may have missing features, and may include data in a form that is difficult to map to a clean [n_samples,n_features] matrix.

One interesting and compelling application of machine learning is to images, and we have already seen a few examples of this where pixel-level features are used for classification.

In this section, we will take a look at one such feature extraction technique, the Histogram of Oriented Gradients (HOG), which transforms image pixels into a vector representation that is sensitive to broadly informative image features regardless of confounding factors like illumination.

```python
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
```

## HOG Features

The Histogram of Gradients is a straightforward feature extraction procedure that was developed in the context of identifying pedestrians within images. HOG involves
the following steps:

1. Optionally prenormalize images. This leads to features that resist dependence on variations in illumination.

2. Convolve the image with two filters that are sensitive to horizontal and vertical brightness gradients. These capture edge, contour, and texture information.

3. Subdivide the image into cells of a predetermined size, and compute a histogram of the gradient orientations within each cell.

4. Normalize the histograms in each cell by comparing to the block of neighboring cells. This further suppresses the effect of illumination across the image.

5. Construct a one-dimensional feature vector from the information in each cell.

A fast HOG extractor is built into the Scikit-Image project, and we can try it out relatively quickly and visualize the oriented gradients within each cell.

Let us use the following code.

```python
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from skimage import data, color, feature
import skimage.data
image = color.rgb2gray(data.chelsea())
hog_vec, hog_vis = feature.hog(image, visualize=True)
fig, ax = plt.subplots(1, 2, figsize=(12, 6),
subplot_kw=dict(xticks=[], yticks=[]))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('input image')
ax[1].imshow(hog_vis)
ax[1].set_title('visualization of HOG features');
plt.show()
```

Then we can see the following image,

![hog_image](../../../../images/ml/hog_image.png)

## HOG in Action: A Simple Face Detector

Using these HOG features, we can build up a simple facial detection algorithm with
any Scikit-Learn estimator; here we will use a linear support vector machine (refer
back to “In-Depth: Support Vector Machines” on page 405 if you need a refresher on
this). The steps are as follows:

1. Obtain a set of image thumbnails of faces to constitute “positive” training samples.

2. Obtain a set of image thumbnails of nonfaces to constitute “negative” training samples.

3. Extract HOG features from these training samples.

4. Train a linear SVM classifier on these samples.

5. For an “unknown” image, pass a sliding window across the image, using the model to evaluate whether that window contains a face or not.

6. If detections overlap, combine them into a single window.

Let’s go through these steps and try it out:

1. Obtain a set of positive training samples.

Let’s start by finding some positive training samples that show a variety of faces.
We have one easy set of data to work with—the Labeled Faces in the Wild dataset,
which can be downloaded by Scikit-Learn:

```python
In[3]: from sklearn.datasets import fetch_lfw_people
faces = fetch_lfw_people()
positive_patches = faces.images
positive_patches.shape
```

Out[3]: (13233, 62, 47)

This gives us a sample of 13,000 face images to use for training.

2. Obtain a set of negative training samples.

Next we need a set of similarly sized thumbnails that do not have a face in them.
One way to do this is to take any corpus of input images, and extract thumbnails
from them at a variety of scales. Here we can use some of the images shipped
with Scikit-Image, along with Scikit-Learn’s PatchExtractor:

```python
In[4]: from skimage import data, transform
imgs_to_use = ['camera', 'text', 'coins', 'moon', 'page', 'clock','immunohistochemistry','chelsea', 'coffee', 'hubble_deep_field']
images = [color.rgb2gray(getattr(data, name)())
for name in imgs_to_use]

In[5]: from sklearn.feature_extraction.image import PatchExtractor
def extract_patches(img, N, scale=1.0,
    patch_size=positive_patches[0].shape):
        extracted_patch_size = \
        tuple((scale * np.array(patch_size)).astype(int))
        extractor = PatchExtractor(patch_size=extracted_patch_size,
        max_patches=N, random_state=0)
        patches = extractor.transform(img[np.newaxis])
        if scale != 1:
            patches = np.array([transform.resize(patch, patch_size) for patch in patches])
        return patches
```