import enum
from sys import stdin
from pprint import pprint
from functools import lru_cache

'''
graph coloring problem

is the graph connected?
not endforced, it could be multiple components.

but there can never be a singleton node, because the format of the input ensures that. it lists pairs of adjacent nodes.
'''

def get_true_count(arr):
    return sum(1 for b in arr if b)

def graph_is_connected(graph):
    # check connectivity
    stack = [0]
    visited = [False] * n
    while len(stack) != 0:
        vertex = stack.pop()
        visited[vertex] = True
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                stack.append(neighbour)

    return all(visited)

def coloring_is_valid(coloring, graph):
    valid_coloring = True
    for node,neighbours in enumerate(graph):
        if not coloring[node] and not any(coloring[n] for n in neighbours):
            valid_coloring = False
            break
    return valid_coloring

def has_colored_neighbour(v, graph, coloring):
    return any(coloring[n] for n in graph[v])

def find_coloring(graph):
    '''
    shit
    '''

    coloring = [0] * len(graph)

    # parents of leaf nodes must be colored
    for i, neighbours in enumerate(graph):
        if len(neighbours) == 1:
            coloring[neighbours[0]] = True

    def color(graph, coloring):
        if coloring_is_valid(coloring, graph):
            return coloring
        else:
            min_result = None

            for v in range(len(graph)):
                if coloring[v] or has_colored_neighbour(v, graph, coloring):
                    continue

                new_coloring = coloring[:]
                new_coloring[v] = 1

                if min_result is not None and sum(new_coloring) >= sum(min_result):
                    continue

                result = color(graph, new_coloring)

                if result is not None:
                    if min_result is None or get_true_count(result) < get_true_count(min_result):
                        min_result = result

            return min_result

    return color(graph, coloring)

def find_coloring2(graph):
    n = len(graph)
    coloring = [0] * n

    # color parents of leaf nodes
    for neighbours in graph:
        if len(neighbours) == 1:
            coloring[neighbours[0]] = 1

    # print('leaves:', coloring)

    best_result = [None]  # list, because it's a hack
    colored_count = [sum(coloring), 0]

    def color(index):
        # at the leaves of the computational tree
        if index == n:
            # print(coloring)
            if coloring_is_valid(coloring, graph):
                if (best_result[0] is None or 
                    colored_count[0] < colored_count[1]):
                    best_result[0] = coloring[:]  # make a copy to preserve this solution
                    colored_count[1] = sum(best_result[0])
            return

        # the current coloring exceed the best result
        if best_result[0] and colored_count[0] >= colored_count[1]:
            return

        # case 1: don't color this node
        color(index + 1)

        # case 2: try coloring this node if not already colored or adjacent to a colored one
        if not coloring[index]: # and not has_colored_neighbour(index, graph, coloring):
            coloring[index] = 1      # make a local change
            colored_count[0] += 1
            color(index + 1)            # apply to subproblems
            colored_count[0] -= 1
            coloring[index] = 0     # backtrack

    color(0)
    return best_result[0]

def find_coloring_bitmask(graph):
    n = len(graph)
    
    # Bitmask: coloring is an integer where bit i = 1 means node i is colored
    coloring = 0
    colored_count = 0

    # Force-color parents of leaf nodes
    for i, neighbors in enumerate(graph):
        if len(neighbors) == 1:
            neighbor = neighbors[0]
            if ((coloring >> neighbor) & 1) == 0:
                coloring |= (1 << neighbor)
                colored_count += 1

    # Sort nodes by descending degree (most constrained first)
    order = sorted(range(n), key=lambda i: -len(graph[i]))

    best_result = [None]  # best bitmask found
    best_count = [float("inf")]

    def is_colored(mask, i):
        return (mask >> i) & 1

    def has_colored_neighbor(v, mask):
        return any(is_colored(mask, u) for u in graph[v])

    def coloring_is_valid(mask):
        for v in range(n):
            if not is_colored(mask, v):
                if not any(is_colored(mask, u) for u in graph[v]):
                    return False
        return True

    def color(index, mask, count):
        if index == n:
            if coloring_is_valid(mask):
                if count < best_count[0]:
                    best_result[0] = mask
                    best_count[0] = count
            return

        # Early pruning
        if count >= best_count[0]:
            return

        v = order[index]

        # Case 1: don't color this node
        color(index + 1, mask, count)

        # Case 2: try coloring this node if not already colored
        if not is_colored(mask, v):  # coloring[v] == 0
            new_mask = mask | (1 << v)
            color(index + 1, new_mask, count + 1)

    color(0, coloring, colored_count)

    # Convert result bitmask to list
    if best_result[0] is None:
        return None
    else:
        final = [(best_result[0] >> i) & 1 for i in range(n)]
        return final

if __name__ == '__main__':
    lines = [[int(a) for a in line.strip().split()] for line in stdin.readlines() if line.strip() != '']

    i = 0
    while i < len(lines):
        n,m = lines[i]
        i += 1
        if n == 0 and m == 0:
            break 

        # print(n, m)

        # construct the graph 
        graph = [[] for _ in range(n)]
        for u,v in lines[i:i+m]:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        # assertion holds in Online Judge
        # assert graph_is_connected(graph), "Graph must be connected."

        coloring = find_coloring_bitmask(graph) 
        # assert coloring is not None, "There must exist a valid coloring."

        # print('coloring:', coloring)
        # print('is valid:', coloring_is_valid(coloring, graph))
        # print('colored:', len([c for c in coloring if c]))
        print(len([c for c in coloring if c]))

        i += m
