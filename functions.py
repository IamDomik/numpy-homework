import math

def task1(x):
    res = 1
    n = len(x)
    m = 0
    if n > 0:
        m = len(x[0])
    for i in range(min(n, m)):
        res *= max(1, x[i][i])
    return res

def task2(x, y):
    if len(x) != len(y): 
        return False
    return sorted(x) == sorted(y)

def task3(x):
    mx = -float('inf')
    fl = False
    for i in range(1, len(x)):
        if x[i - 1] == 0 and x[i] > mx:
            mx = x[i]
            fl = True
    if fl:
        return mx
    return None

def task4(img, weights):
    h, w, c = len(img), len(img[0]), len(img[0][0])
    res = [[0.0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            s = 0.0
            for k in range(c):
                s += img[i][j][k] * weights[k]
            res[i][j] = s
    return res

def task5(x):
    if not x: return [], []
    ans, cnt = [], []
    val, c = x[0], 1
    for i in range(1, len(x)):
        if x[i] == val:
            c += 1
        else:
            ans.append(val)
            cnt.append(c)
            val, c = x[i], 1
    ans.append(val)
    cnt.append(c)
    return ans, cnt

def task6(X, Y):
    n, m = len(X), len(Y)
    dist = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            d = 0.0
            for k in range(len(X[i])):
                d += (X[i][k] - Y[j][k]) ** 2
            dist[i][j] = math.sqrt(d)
    return dist
