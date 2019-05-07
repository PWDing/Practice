from collections import deque


def bfs(graph, key):
    search_queue = deque()
    search_queue += graph[key]
    searched = []

    while search_queue:
        node = search_queue.popleft()
        if node not in searched:
            if is_need(node):
                print("{} is needed.".format(node.title()))
                return True
            else:
                search_queue += graph[node]
                searched.append(node)
    return False


def is_need(string):
    return string[0] == 'p'


def dijkstra(graph, costs, parents):
    cost = 0
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for key in neighbors.keys():
            new_cost = cost + neighbors[key]
            if new_cost < costs[key]:
                costs[key] = new_cost
                parents[key] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    # display the shortest path
    path = ['end']
    while path[-1]:
        path.append(parents[path[-1]])
    # delete 'None' element
    path.pop()
    # make the path in right order
    path.reverse()
    shortest_path = {'path': path, 'cost': cost}
    return shortest_path


def find_lowest_cost_node(node_costs, done):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node, cost in node_costs.items():
        if cost < lowest_cost and node not in done:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


path_graph = {
    'start': {'a': 6, 'b': 2},
    'a': {'end': 1},
    'b': {'a': 3, 'end': 5},
    'end': {}
}
expense = {'a': 6, 'b': 2, 'end': float('inf')}
father = {'start': None, 'a': 'start', 'b': 'start', 'end': None}

print(dijkstra(path_graph, expense, father))
