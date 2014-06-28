Quick and dirty implementation of [Dijkstra's algorithm](http://en.wikipedia.org/wiki/Dijkstra's_algorithm) for finding shortest path distances in a connected graph.

This implementation has a *O((m+n) log n)* running time, where *n* is the number of
vertices and *m* is the number of edges. If the graph is connected (i.e. in one piece), *m* normally dominates over *n*, making the algorithm *O(m log n)* overall.

The main function takes as arguments a graph structure and a starting vertex.  

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
