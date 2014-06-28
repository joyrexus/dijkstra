Quick and dirty implementation of [Dijkstra's algorithm](http://en.wikipedia.org/wiki/Dijkstra's_algorithm) for finding shortest path distances in a connected graph.

This implementation should have a *O((m+n) log n)* running time, where *n* is the number of
vertices and *m* is the number of edges. If the graph is connected (i.e. in one piece), *m* normally dominates over *n*, making the algorithm *O(m log n)* overall.


```python
graph = {'a': {'b': 1}, 
         'b': {'c': 2, 'b': 5}, 
         'c': {'d': 1},
         'd': {}}
```

Get shortest path distances to each node in `graph` from `a`:

```python
dist, pred = dijkstra(graph, 'a') 
assert dist == {'a': 0, 'c': 3, 'b': 1, 'd': 4}
```
