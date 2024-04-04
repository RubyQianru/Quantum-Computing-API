# NumPy

NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
NumPy stands for Numerical Python.

- [NumPy Documentation: NumPy user guide](https://numpy.org/doc/stable/user/index.html)
- [w3school: NumPy Tutorial](https://www.w3schools.com/python/numpy/default.asp)

### Setup Environment: Download Miniconda / Conda
- [Download Miniconda](https://docs.anaconda.com/free/miniconda/index.html)

### Install NumPy

If you use pip, you can install NumPy with:

```
pip install numpy
```

## NumPy Fundamentals

Getting started:

```python

import numpy as np

```

### Array Creation

```python

a1D = np.array([1, 2, 3, 4])
a2D = np.array([[1, 2], [3, 4]])
a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

```
### Array Shape

The shape of an array is the number of elements in each dimension.

The example returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.

```python

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

```



### Array Reshape

The example reshapes a 1-D array to a 2-D array. The outermost dimension will have 4 arrays, each with 3 elements.

```python

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)

print(newarr)

```


### Array Search

The example finds the indexes where the value is 4:

```python

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

```

# Fast API


### Inatall the Server Program

```
pip install "uvicorn[standard]"
```

