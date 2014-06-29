Quick and dirty implementation of [Dijkstra's algorithm](http://en.wikipedia.org/wiki/Dijkstra's_algorithm) for finding shortest path distances in a connected graph.

This implementation has a *O((m+n) log n)* running time, where *n* is the number of
vertices and *m* is the number of edges. If the graph is connected (i.e. in one piece), *m* normally dominates over *n*, making the algorithm *O(m log n)* overall.

## Usage

```python
from dijkstra import dijkstra, shortest_path
```

The main function takes as arguments a graph structure and a starting vertex.  

```python
dist, pred = dijkstra(graph, start='a') 
```

The graph structure should be a dict of dicts, a mapping of each node `v` to its
successor nodes `w` and their respective edge weights (`v -> w`).


```python
graph = {'a': {'b': 1}, 
         'b': {'c': 2, 'b': 5}, 
         'c': {'d': 1},
         'd': {}}

dist, pred = dijkstra(graph, start='a') 
```

It returns two dicts, `dist` and `pred`:
    
`dist` is a dict mapping each node to its shortest distance from the specified starting node:

```python
assert dist == {'a': 0, 'c': 3, 'b': 1, 'd': 4}
```

`pred` is a dict mapping each node to its predecessor node on the shortest path from the specified starting node:

```python
assert pred == {'b': 'a', 'c': 'b', 'd': 'c'}
```

The `dijkstra` function allows us to easily compute shortest paths between two
nodes in a graph.  The `shortest_path` function is provided as a convenience:

```python
graph = {'a': {'b': 1}, 
         'b': {'c': 2, 'b': 5}, 
         'c': {'d': 1},
         'd': {}}

assert shortest_path(graph, 'a', 'a') == ['a']
assert shortest_path(graph, 'a', 'b') == ['a', 'b']
assert shortest_path(graph, 'a', 'c') == ['a', 'b', 'c']
assert shortest_path(graph, 'a', 'd') == ['a', 'b', 'c', 'd']
```


## See Also

Other implementations using an [indexed priority queue](https://github.com/nvictus/priority-queue-dictionary#what-is-an-indexed-priority-queue):

* [Variant 1](http://code.activestate.com/recipes/119466-dijkstras-algorithm-for-shortest-paths/)
* [Variant 2](https://github.com/nvictus/priority-queue-dictionary/blob/master/examples/dijkstra.py)
