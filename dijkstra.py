def dijkstra(graph, costs, parents, processed):
    # 找到未处理节点中开销最低的节点
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        # 更新该节点的邻居的开销
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return costs['end']


def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


nodes = {
    'start': {'a': 5, 'b': 2},
    'a': {'c': 4, 'd': 2},
    'b': {'a': 8, 'd': 7},
    'c': {'d': 6, 'end': 3},
    'd': {'end': 1},
    'end': {}
}
infinity = float('inf')
expense = {'a': 5, 'b': 2, 'c': infinity, 'd': infinity, 'end': infinity}
father = {'a': 'start', 'b': 'start', 'c': None, 'd': None, 'end': None}
done = []

print(dijkstra(nodes, expense, father, done))
