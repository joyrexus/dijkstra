from nose.tools import assert_raises
from dijkstra import dijkstra, shortest_path, make_graph


def test_make_graph():
    '''
    Test `make_graph` function.

    '''
    G = make_graph('test_data/undirected.txt')
    assert G['A']['B'] == 1
    assert G['B']['A'] == 1
    assert G['A']['C'] == 5
    assert G['C']['A'] == 5
    assert_raises(KeyError, G['A'].__getitem__, 'D')
    assert_raises(KeyError, G['D'].__getitem__, 'A')

    G = make_graph('test_data/directed.txt')
    assert G['A']['B'] == 1
    assert G['A']['C'] == 5
    assert G['B']['C'] == 2
    assert_raises(KeyError, G['B'].__getitem__, 'A')


def test_dijkstra():
    '''
    Test `dijkstra` function.
    
    This is an implementation of dijkstra's algorithm
    for finding shortest path distances to all nodes 
    in a graph from a specified start node.

    '''
    G = make_graph('test_data/undirected.txt')
    expected = {'A': 0, 'C': 3, 'B': 1, 'D': 4}
    dist, pred = dijkstra(G, 'A')
    assert dist == expected

    G = make_graph('test_data/directed.txt')
    dist, pred = dijkstra(G, 'A')
    assert dist == expected

    graph = {'a': {'b': 1}, 
             'b': {'c': 2, 'b': 5}, 
             'c': {'d': 1},
             'd': {}}
    dist, pred = dijkstra(graph, start='a')
    assert dist == {'a': 0, 'c': 3, 'b': 1, 'd': 4}
    assert pred == {'b': 'a', 'c': 'b', 'd': 'c'}


def test_shortest_path():
    '''
    Get shortest path distances from start to end node.

    '''
    graph = {'a': {'b': 1}, 
             'b': {'c': 2, 'b': 5}, 
             'c': {'d': 1},
             'd': {}}
    assert shortest_path(graph, 'a', 'a') == ['a']
    assert shortest_path(graph, 'a', 'b') == ['a', 'b']
    assert shortest_path(graph, 'a', 'c') == ['a', 'b', 'c']
    assert shortest_path(graph, 'a', 'd') == ['a', 'b', 'c', 'd']

    graph = {'a': {'b':14, 'c':9, 'd':7},
             'b': {'a':14, 'c':2, 'e':9},
             'c': {'a':9, 'b':2, 'd':10, 'f':11},
             'd': {'a':7, 'c':10, 'f':15},
             'e': {'b':9, 'f':6},
             'f': {'c':11, 'd':15, 'e':6}}
    assert shortest_path(graph, 'a', 'e') == ['a', 'c', 'b', 'e']


def test_answer():
    '''
    Get the shortest-path distances to the following ten vertices
    from the graph specified in `test/data.txt`, in order: 
    7,37,59,82,99,115,133,165,188,197. 

    Returns a comma-separated string of integers containing the results
    for each vertex in the specified order.

    '''
    G = make_graph('test_data/data.txt')
    dist, pred = dijkstra(G, '1')
    ends  = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197] # ending vertices
    results = [str(dist[str(x)]) for x in ends]
    answer = ','.join(results)
    expected = '2599,2610,2947,2052,2367,2399,2029,2442,2505,3068'
    assert answer == expected
