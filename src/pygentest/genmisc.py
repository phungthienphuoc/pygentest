from .gensequence import randlist_uniqueint
from random import shuffle, choices, randint

def randperm(n, k):
    """Get a random permutation of `k` number chosen from base set `{1,2,...,n}`.

    Args:
        `n`: Size of base set.
        `k`: Size of permutation.
    """
    return randlist_uniqueint(k, 1, n)

def randpartition_integer(n, k):
    """Randomly partition positive integer `n` into `k` summands.

    Args:
        `n`: Partitioned number.
        `k`: Number of summands.
    """
    if n <= 0:
        raise ValueError("The partitioned number must be positive.")
    if k <= 0:
        raise ValueError("The number of summands must be positive.")
    if n < k:
        raise ValueError("The number of summands must not exceed the partitioned number.")
    cummulation = randlist_uniqueint(k-1,1,n-1,sorted=True)
    cummulation.append(n)
    res = []
    prev = 0
    for x in cummulation:
        res.append(x-prev)
        prev = x
    return res

def randpartition_set(baseset, k):
    """Randomly partition `baseset` into `k` subsets.

    Args:
        `baseset`: Base set.
        `k`: Number of summands.
    """
    if k <= 0:
        raise ValueError("The number of subsets must be positive.")
    if len(baseset) < k:
        raise ValueError("The number of subsets must not exceed the size of base set.")
    new = list(baseset)
    shuffle(new)
    count = randpartition_integer(len(baseset),k)
    cur = []
    res = []
    while count:
        for _ in range(count.pop()):
            cur.append(new.pop())
        res.append(cur)
        cur = []
    return res

def __coordinate(n, axis, cmin, cmax):
    crange = cmax-cmin+1
    weight = [(crange-n+1)/n,1,(n-1)/(crange-n+2)]
    if crange < n:
        weight[0] = 0
    if crange < n-1:
        weight[1] = 0
    if crange < n-2 or n==3:
        weight[2] = 0
    if sum(weight) == 0:
        raise ValueError(f"Range of {axis}-coordinate is not large enough for polygon.")
    zero = choices((0,1,2),weight)
    val = randlist_uniqueint(n-zero, cmin, cmax, sorted=True)
    pos,neg = [val[0]],[val[0]]
    for i in range(1,len(val)-1):
        if randint(0,1):
            pos.append(val[i])
        else:
            neg.append(val[i])
    pos.append(val[-1])
    neg.append(val[-1])
    res = []
    for i in range(1,len(pos)):
        res.append(pos[i]-pos[i-1])
    for i in range(1,len(neg)):
        res.append(neg[i-1]-neg[i])
    res.extend([0]*zero)
    shuffle(res)
    return res, val[-1]-val[0]

def __quadrant(x,y):
    if x >= 0 and y >= 0:
        return 1
    if x >= 0:
        return 3
    if y >= 0:
        return 2
    return 4

def randpolygon_lattice(n, minX, maxX, minY, maxY):
    """Get a random lattice polygon with `n` vertices.

    Args:
        `n`: Number of vertices.
        `minX`: Lowerbound of x-coordinate.
        `maxX`: Upperbound of x-coordinate.
        `minY`: Lowerbound of y-coordinate.
        `maxY`: Upperbound of y-coordinate.
    """
    if n <= 2:
        raise ValueError("Polygon must have at least 3 vertices.")
    if maxX <= minX:
        raise ValueError("maxX must be greater than minX")
    if maxY <= minY:
        raise ValueError("maxY must be greater than minY")
    vecx,rangeX = __coordinate(n, 'x', minX, maxX)
    vecy,rangeY = __coordinate(n, 'y', minY, maxY)
    edges = [(x,y) for x,y in zip(vecx,vecy)]
    edges.sort(key=lambda x,y: (__quadrant(x,y), y/x))
    idx = bound = 0
    while idx < n and __quadrant(*edges[idx]) == 1:
        bound += edges[idx][1]
        idx += 1
    curY = randint(minY, maxY-rangeY)
    curX = randint(minX+rangeX-bound,maxX-bound)
    vertices = []
    for dx,dy in edges:
        vertices.append((curX,curY))
        curX += dx
        curY += dy
    shuffle(vertices)
    return vertices