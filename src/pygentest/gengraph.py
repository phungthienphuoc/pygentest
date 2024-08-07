from random import choices, randrange, random, shuffle
from .wrapper import Wrapper
from .gensequence import randlist_uniqueint

def __randgraph_undirected(V, E, _1_indexed, loop):
    edges = []
    weight = [i+loop for i in range(V)]
    wrap = Wrapper(choices, (i for i in range(V)), weight)
    chosen = [{} for _ in range(V)]
    for _ in range(E):
        v1 = wrap()
        temp = randrange(weight[v1])
        v2 = chosen[v1-1].get(temp, temp)
        chosen[v1][v2] = weight[v1]
        weight[v1] -= 1
        v1 += _1_indexed
        v2 += _1_indexed
        edges.append((v1,v2) if randrange(2) else (v2,v1))
    return edges

def __randgraph_directed(V, E, _1_indexed, loop):
    edges = []
    dividend = V-1+loop
    idx = randlist_uniqueint(E, 0, V*dividend-1)
    for x in idx:
        v1 = x // dividend
        v2 = x % dividend
        if v1 == v2 and not loop:
            v2 = V-1
        v1 += _1_indexed
        v2 += _1_indexed
        edges.append((v1,v2) if randrange(2) else (v2,v1))
    return edges

def randgraph(V, E, /, directed=False, loop=False, *, _1_indexed=True):
    """Get edge list of a random graph with `V` vertices and `E` edges.

    Args:
        `V`: Number of vertices.
        `E`: Number of edges.
        `directed`: `True` if graph is directed. Defaults to `False`.
        `loop`: `True` if graph allows loop. Defaults to `False`.
        `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
    """
    if V <= 0:
        raise ValueError("The number of vertices must be positive.")
    if E < 0:
        raise ValueError("The number of edges must be non negative.")
    if (directed and E>V*(V-1)) or (not directed and E>V*(V-1)//2):
        raise ValueError("The number of edges exceeds the maximum value.")
    if directed:
        return __randgraph_directed(V, E, _1_indexed, loop)
    else:
        return __randgraph_undirected(V, E, _1_indexed, loop)
    
def randgraph_probability(V, /, p=0.5, directed=False, loop=False, *, _1_indexed=True):
    """Get edge list of a random graph with `V` vertices, and the probability for each
    pair of vertices to be connected is `p`. 

    Args:
        `V`: Number of vertices.
        `p`: Probability for each pair of vertices to be connected. Defaults to `0.5`.
        `directed`: `True` if graph is directed. Defaults to `False`.
        `loop`: `True` if graph allows loop. Defaults to `False`.
        `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
    """
    if V <= 0:
        raise ValueError("The number of vertices must be positive.")
    edges = []
    for i in range(V+_1_indexed):
        for j in range(V+_1_indexed if directed else i+loop):
            if j==i and not loop:
                continue
            if random()>p:
                edges.append((i,j) if randrange(2) else (j,i))
    return edges

def randmultigraph(V, E, /, loop=False,  *, _1_indexed=True):
    """Get edge list of a random multigraph with `V` vertices and `E` edges.

    Args:
        `V`: Number of vertices.
        `E`: Number of edges.
        `loop`: `True` if graph allows loop. Defaults to `False`.
        `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
    """
    if V <= 0:
        raise ValueError("The number of vertices must be positive.")
    if E < 0:
        raise ValueError("The number of edges must be non negative.")
    edges = []
    weight = [i+loop for i in range(V)]
    wrap = Wrapper(choices, (i for i in range(V)), weight)
    chosen = [{} for _ in range(V)]
    for _ in range(E):
        v1 = wrap()
        temp = randrange(weight[v1])
        v2 = chosen[v1].get(temp, temp)
        chosen[v1][v2] = weight[v1]
        weight[v1] -= 1
        v1 += _1_indexed
        v2 += _1_indexed
        edges.append((v1,v2) if randrange(2) else (v2,v1))
    return edges
            
def randtree_rooted(V, *, _1_indexed=True):
    """Get list of parent vertex of each vertex in a random rooted tree.
    
    The tree is rooted at vertex 1 if the verticed are 1-indexed, and 0, otherwise.

    Args:
        `V`: Number of vertices.
        `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
    """
    if V <= 0:
        raise ValueError("The number of vertices must be positive.")
    parent = [0]*(V-1)
    chosen = [int(_1_indexed)]
    rest = randlist_uniqueint(V,1+_1_indexed, V-1+_1_indexed)
    for _ in range(V-1):
        node = rest.pop()
        par = choices(chosen)
        parent[node] = par
        chosen.append(node)
    return parent

def randtree(V, *, _1_indexed=True):
    """Get edge list of a random tree with `V` vertices.

    Args:
        `V`: Number of vertices.
        `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
    """
    if V <= 0:
        raise ValueError("The number of vertices must be positive.")
    rooted = randtree_rooted(V, _1_indexed=_1_indexed)
    swap = randlist_uniqueint(V,_1_indexed,V-1+_1_indexed)
    edges = []
    for i in range(V-1):
        v1 = swap[i]+_1_indexed
        v2 = rooted[i]
        edges.append((v1,v2) if randrange(2) else (v2,v1))
    return edges

def randgraph_connected(V, E, *, _1_indexed=True):
    """Get edge list of a random connected undirected graph with `V` vertices and `E` edges.

    Args:
        `V`: Number of vertices.
        `E`: Number of edges.
        `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
    """
    if V <= 0:
        raise ValueError("The number of vertices must be positive.")
    if E < 0:
        raise ValueError("The number of edges must be non negative.")
    if E < V-1:
        raise ValueError("The number of edges is not enough to form a connected graph.")
    edges = randtree(V, _1_indexed=False)
    weight = [i for i in range(V)]
    chosen = [{} for _ in range(V)]
    for i in range(V-1):
        a,b = edges[i]
        edges[i] = (a+_1_indexed,b+_1_indexed)
        if a < b:
            a,b = b,a
        chosen[a][b] = weight[a]
        weight[a] -= 1
    wrap = Wrapper(choices, (i for i in range(V)), weight)
    for _ in range(E-V+1):
        v1 = wrap()
        temp = randrange(weight[v1])
        v2 = chosen[v1].get(temp, temp)
        chosen[v1][v2] = weight[v1]
        weight[v1] -= 1
        v1 += _1_indexed
        v2 += _1_indexed
        edges.append((v1,v2) if randrange(2) else (v2,v1))
    shuffle(edges)
    return edges
    
def randDAG(V, E, /, connected=True, *, _1_indexed=True):
    """Get edge list of a random directed acyclic graph with `V` vertices and `E` edges.

    Args:
        `V`: Number of vertices.
        `E`: Number of edges.
        `connected`: `True` if graph is (weakly) connected. Defaults to `True`.
        `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
    """
    if V <= 0:
        raise ValueError("The number of vertices must be positive.")
    if E < 0:
        raise ValueError("The number of edges must be non negative.")
    if connected:
        edges = randgraph_connected(V, E, _1_indexed=False)
    else:
        edges = randgraph(V, E, _1_indexed=False)
    swap = randlist_uniqueint(V, 0, V-1)
    for i in range(E):
        a,b = edges[i]
        if a>b:
            a,b=b,a
        edges[i] = (swap[a]+_1_indexed,swap[b]+_1_indexed)
    return edges