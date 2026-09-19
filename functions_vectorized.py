import numpy as np

def task1(x):
    diag = np.diagonal(x)
    ans = diag[diag != 0]
    if len(ans) == 0:
        return 1
    return np.prod(ans)

def task2(x, y):
    if len(x) != len(y): 
        return False
    return np.array_equal(np.sort(x), np.sort(y))

def task3(x):
    c = x[1:][x[:-1] == 0]
    if len(c) == 0:
        return None
    return np.max(c)

def task4(img, weights):
    return np.sum(img * weights, axis=-1)

def task5(x):
    change_indices = np.where(x[1:] != x[:-1])[0] + 1
    boundaries = np.concatenate(([0], change_indices, [len(x)]))
    values = x[boundaries[:-1]]
    counts = np.diff(boundaries)
    return values, counts

def task6(X, Y):
    diff = X[:, np.newaxis, :] - Y[np.newaxis, :, :]
    return np.sqrt(np.sum(diff ** 2, axis=-1))
