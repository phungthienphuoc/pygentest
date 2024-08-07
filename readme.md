<h2> pygentest - Python test generators </h2>

<p>
This is a Python library supporting several data generators. They can be use for test generation in Competitive Programming, or exams, etc.
</p>

<p>
This project has not been released yet, and still in progess. If you want to try and test this library, you can install it by using pip install:

```
pip install -i https://test.pypi.org/simple/ pygentest
```
</p>

<div>
<h3>Here is the list of supported function:</h3>
<ul>
    <li>
        <a href=#0><strong>Wrapper</strong></a>
        <br/>
        <a href=#0-1>
            <code>class Wrapper(func, *args, **kwargs)</code>
        </a>
        <ul>
            <li>
            <a href=#0-1-1>
            <code>__call__()</code>
            </a>
            </li>
        </ul>
    </li>
    <li>
        <a href=#1><strong>Value generators</strong></a>
        <ol>
            <li>
                <a href=#1-1>
                    <code>randint</code>
                </a>
            </li>
            <li>
                <a href=#1-2>
                    <code>randfloat</code>
                </a>
            </li>
            <li>
                <a href=#1-3>
                    <code>randchar</code>
                </a>
            </li>
        </ol>
    </li>
    <li>
        <a href=#2><strong>Sequence generators</strong></a>
        <ol>
            <li>
                <a href=#2-1>
                    <code>randlist_any</code>
                </a>
            </li>
            <li>
                <a href=#2-2>
                    <code>randlist_uniqueint</code>
                </a>
            </li>
            <li>
                <a href=#2-3>
                    <code>randmatrix_any</code>
                </a>
            </li>
            <li>
                <a href=#2-4>
                    <code>randstring</code>
                </a>
            </li>
            <li>
                <a href=#2-5>
                    <code>randlist_string</code>
                </a>
            </li>
        </ol>
    </li>
    <li>
        <a href=#3><strong>Graph generators</strong></a>
        <ol>
            <li>
                <a href=#3-1>
                    <code>randgraph</code>
                </a>
            </li>
            <li>
                <a href=#3-2>
                    <code>randgraph_probability</code>
                </a>
            </li>
            <li>
                <a href=#3-3>
                    <code>randmultigraph</code>
                </a>
            </li>
            <li>
                <a href=#3-4>
                    <code>randtree_rooted</code>
                </a>
            </li>
            <li>
                <a href=#3-5>
                    <code>randtree</code>
                </a>
            </li>
            <li>
                <a href=#3-6>
                    <code>randgraph_connected</code>
                </a>
            </li>
            <li>
                <a href=#3-7>
                    <code>randDAG</code>
                </a>
            </li>
        </ol>
    </li>
    <li>
        <a href=#4><strong>Miscellaneous generators</strong></a>
        <ol>
            <li>
                <a href=#4-1>
                    <code>randperm</code>
                </a>
            </li>
            <li>
                <a href=#4-2>
                    <code>randpartition_integer</code>
                </a>
            </li>
            <li>
                <a href=#4-3>
                    <code>randpartition_set</code>
                </a>
            </li>
            <li>
                <a href=#4-4>
                    <code>randpolygon</code>
                </a>
            </li>
        </ol>
    </li>
</ul>
</div>

<div>
<h3 id="0">Wrapper</h3>
<code id="0-1">class Wrapper(func, *args, **kwargs)</code>

Wrapper of a function.

It could be used to reduce repetition of calling a function with the same arguments.

Args:
- `func`: The function needs to be wrapped.
- `*args`: The positional arguments of `func`.
- `**kwargs`: The keyword arguments of `func`.

Example:
```
>>> from pygentest import *
>>> f = Wrapper(randint, 1, 10)
>>> f()
3

>>> f()
6
```

**List of methods:**
<ul>
<li>
<code id="0-1-1"> __call__() </code>

Call the instance as the wrapped function.
</li>
</ul>
</div>
<br/>
<div>
<h3 id="1"> Value generators</h3>
<ol>

<li>
<code id="1-1">randint(a, b)</code>

Get a random integer in inclusive range [a,b].

In fact, it is alias for [`random.randint`](https://docs.python.org/3/library/random.html#random.randint).

Args:
- `a`: Lowerbound of range.
- `b`: Upperbound of range.
</li>
<br/>
<li>
<code id="1-2">randfloat(a, b)</code>

Get a random number in the range [a, b) or [a, b] depending on rounding.

In fact, it is alias for [`random.uniform`](https://docs.python.org/3/library/random.html#random.uniform).

Args:
- `a`: Lowerbound of range.
- `b`: Upperbound of range.
</li>
<br/>
<li>
<code id="1-3">randchar(chars)</code>

Get a random character from the given list of character.
    
Args:
- `chars`: List of character.
</li>
</ol>
</div>
<br/>
<div>
<h3 id="2"> Sequence generators</h3>
<ol>

<li>
<code id="2-1">
randlist_any(size, wrapgen, sorted=False, reverse=False)
</code>

Get a random list of length `size`, with elements generated by `wrapgen`.

Note: `wrapgen` must have type [`Wrapper`](#0-1).

Args:
- `size`: Length of list.
- `wrapgen`: Wrapped generator for elements.
- `sorted`: `True` if the returned list is sorted. Defaults to `False`.
- `reverse`: `True` if the returned list is sorted in descending order. Defaults to `False`.
</li>
<br/>
<li>
<code id="2-2">randlist_uniqueint(size, a, b, sorted=False, reverse=False)</code>

Get a random list of unique integers in inclusive range [a,b].

The algorithm used to implement this function is inspired by [Knuth shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle).

Args:
- `size`: Length of list.
- `a`: Lower bound of the range.
- `b`: Upper bound of the range.
- `sorted`: `True` if the returned list is sorted. Defaults to `False`.
- `reverse`: `True` if the returned list is sorted in descending order. Defaults to `False`.
</li>
<br/>
<li>
<code id="2-3">randmatrix_any(numrow, numcol, wrapgen)</code>

Get a random list of size `numrow` by `numcol`, with elements generated by `wrapgen`.

Note: `wrapgen` must have type [`Wrapper`](#0-1).

Args:
- `numrow`: Number of rows.
- `numcol`: Number of columns.
- `wrapgen`: Wrapped generator for elements.
</li>
<br/>
<li>
<code id="2-4">randstring(length, chars)</code>

Get a random string of length `length` whose characters randomly chosen from `chars`.

Args:
- `length`: Length of string.
- `chars`: List of characters.
</li>
<br/>
<li>
<code id="2-5">randlist_string(size, length, chars)</code>

Get a random list of `size` strings of length `length` with characters from `chars`.

Args:
- `size`: Length of list.
- `length`: Length of each string.
- `chars`: List of characters.
</li>

</ol>
</div>
<br/>

<div>
<h3 id="3"> Graph generators</h3>
<ol>

<li>
<code id="3-1">
randgraph(V, E, /, directed=False, loop=False, *, _1_indexed=True)
</code>

Get edge list of a random graph with `V` vertices and `E` edges.

An error will be raise if `V` is non-positive, or less

Args:
- `V`: Number of vertices.
- `E`: Number of edges.
- `directed`: `True` if graph is directed. Defaults to `False`.
- `loop`: `True` if graph allows loop. Defaults to `False`.
- `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
</li>
<br/>
<li>
<code id="3-2">randlist_uniqueint(size, a, b, sorted=False, reverse=False)</code>

Get edge list of a random graph with `V` vertices, and the probability for each pair of vertices to be connected is `p`. 

Args:
- `V`: Number of vertices.
- `p`: Probability for each pair of vertices to be connected. Defaults to `0.5`.
- `directed`: `True` if graph is directed. Defaults to `False`.
- `loop`: `True` if graph allows loop. Defaults to `False`.
- `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
</li>
<br/>
<li>
<code id="3-3">randmultigraph(V, E, /, loop=False,  *, _1_indexed=True)</code>

Get edge list of a random multigraph with `V` vertices and `E` edges.

Args:
- `V`: Number of vertices.
- `E`: Number of edges.
- `loop`: `True` if graph allows loop. Defaults to `False`.
- `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
</li>
<br/>
<li>
<code id="3-4">randtree_rooted(V, *, _1_indexed=True)</code>

Get list of parent vertex of each vertex in a random rooted tree.

The tree is rooted at vertex 1 if the verticed are 1-indexed, and 0, otherwise.

Args:
- `V`: Number of vertices.
- `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
</li>
<br/>
<li>
<code id="3-5">randtree(V, *, _1_indexed=True)</code>

Get edge list of a random tree with `V` vertices.

This function is constructed based on [`randtree_rooted`](#3-4).

Args:
- `V`: Number of vertices.
- `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
</li>
<br/>
<li>
<code id="3-6">randgraph_connected(V, E, *, _1_indexed=True)</code>

Get edge list of a random connected undirected graph with `V` vertices and `E` edges.

This function is constructed based on [`randtree`](#3-5).

Args:
- `V`: Number of vertices.
- `E`: Number of edges.
- `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
</li>
<br/>
<li>
<code id="3-7">randDAG(V, E, /, connected=True, *, _1_indexed=True)</code>

Get edge list of a random directed acyclic graph with `V` vertices and `E` edges.

This function is constructed based on [`randgraph`](#3-1) and [`randgraph_connected`](#3-6).

Args:
- `V`: Number of vertices.
- `E`: Number of edges.
- `connected`: `True` if graph is (weakly) connected. Defaults to `True`.
- `_1_indexed`: `True` if vertices are 1-indexed. Defaults to `True`.
</li>
</ol>
</div>
<br/>

<div>
<h3 id="4"> Miscellaneous generators</h3>
<ol>

<li>
<code id="4-1">
randperm(n, k)
</code>

Get a random permutation of `k` number chosen from base set `{1,2,...,n}`

Args:
- `n`: Size of base set.
- `k`: Size of permutation.
</li>
<br/>
<li>
<code id="4-2">randpartition_integer(n, k)</code>

Randomly partition positive integer `n` into `k` summands.

Here is more information about [integer partition](https://en.wikipedia.org/wiki/Integer_partition).

Args:
- `n`: Partitioned number.
- `k`: Number of summands.
</li>
<br/>
<li>
<code id="4-3">randpartition_set(baseset, k)</code>

Randomly partition `baseset` into `k` subsets.

Here is more information about [partition of a set](https://en.wikipedia.org/wiki/Partition_of_a_set).

Args:
- `baseset`: Base set.
- `k`: Number of summands.
</li>
<br/>
<li>
<code id="4-4">randpolygon_lattice(n, minX, maxX, minY, maxY)</code>

Get a random lattice polygon with `n` vertices.

A lattice polygon is a polygon whose every vertex has integer coordinates.

Args:
- `n`: Number of vertices.
- `minX`: Lowerbound of x-coordinate.
- `maxX`: Upperbound of x-coordinate.
- `minY`: Lowerbound of y-coordinate.
- `maxY`: Upperbound of y-coordinate.
</li>
<br/>
</ol>
</div>
<br/>