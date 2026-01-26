import sys

"""
TOO SLOW

NOT_REACHED = -2
COLORED_UNREACHED = -1

def all_reached(reached):
    for r in reached:
        if r == NOT_REACHED:
            return False
    return True

def stations_color(graph, idx, n, colored, colored_count, min_count, reached):

    if all_reached(reached):  
        return colored_count
    elif colored_count >= min_count:
        return min_count
    elif idx == n:
        return min_count
    else:
        # case 1: dont color
        didnt_color_count = stations_color(graph, idx + 1, n, colored, colored_count, min_count, reached)
        min_count = min(min_count, didnt_color_count)

        # case 2: color
        if not colored[idx] and colored_count + 1 < min_count:
            # color vertex
            colored[idx] = True
            colored_count += 1

            # if its not reached, then set that it is colored
            # thus new vertex was reached
            if reached[idx] == NOT_REACHED:
                reached[idx] = COLORED_UNREACHED
                new_vert_reached = True
            else:
                new_vert_reached = False

            # set every of its non reached neigh to it
            for neigh in graph[idx]:
                if reached[neigh] == NOT_REACHED:
                    reached[neigh] = idx
                    new_vert_reached = True

            # only if new vertex was reached it makes sense to recurse
            if new_vert_reached:
                did_color_count = stations_color(graph, idx + 1, n, colored, colored_count, min_count, reached)
                min_count = min(min_count, did_color_count)

            # backtrack
            for neigh in graph[idx]:
                if reached[neigh] == idx:
                    reached[neigh] = NOT_REACHED

            if reached[idx] == COLORED_UNREACHED:
                reached[idx] = NOT_REACHED

            colored_count -= 1
            colored[idx] = False


        return min_count

def stations(graph):
    n = len(graph)
         
    colored = [False] * n
    idx = 0
    min_count = float('+inf')
    colored_count = 0
    reached = [-2] * n

    # precolor singleton and leaves' parents
    for v in range(n):   
        if not colored[v]:
            if len(graph[v]) == 0:
                colored[v] = True
                colored_count += 1
                reached[v] = COLORED_UNREACHED
            elif len(graph[v]) == 1 and not colored[graph[v][0]]:
                parent = graph[v][0]
                colored[parent] = True
                colored_count += 1
                reached[parent] = COLORED_UNREACHED
                for neigh in graph[parent]:
                    if reached[neigh] == NOT_REACHED:
                        reached[neigh] = parent

    return stations_color(graph, idx, n, colored, colored_count, min_count, reached)
"""


'''
[1 0 0 1]  # node 4 and node 1 are connected
[0 1 0 0]  # every node is connected to itself
[0 0 1 0]
[0 1 0 1]  # node 2 and node 4 are connected
'''

def print_connections(connections):
    n = len(connections)
    format_string = f"{{0:0{n}b}}"
    for connection in connections:
        print(format_string.format(connection))

def stations_color(connections, reachable_when_skip, all_reached, reached, current_count, best_count, idx, n):
    if reached == all_reached:
        return current_count
    elif current_count >= best_count:
        return best_count
    elif idx == n:
        return best_count
    else:
        # case 1: skip if skipping this node results in an subinstance that is still reachable
        if (reached | reachable_when_skip[idx]) == all_reached:
            best_count = min(best_count, stations_color(
                connections, 
                reachable_when_skip, 
                all_reached, 
                reached, 
                current_count, 
                best_count, 
                idx + 1, 
                n,
            ))

        # case 2: color
        reached_when_colored = reached | connections[idx]

        # if coloring this node, changed the reach then evaluate it and see if it leads to a more optimal solution
        if reached != reached_when_colored:
            best_count = min(best_count, stations_color(
                connections, 
                reachable_when_skip, 
                all_reached, 
                reached_when_colored, 
                current_count + 1, 
                best_count, 
                idx + 1, 
                n,
            ))

        return best_count
   
# returns the number of bits in 'seq' that are 1. Check up to 'seq_len' from the right.
def nbits_set(seq, n, seq_len):
    ones = 0
    for i in range(seq_len):
        if seq >> i & 1 == 1:
            ones += 1
        if ones > n:
            return False
    return True

def stations(connections):
    n = len(connections)
    
    # this structure answers: If I skip i-th node, can I still reach every node in the graph?
    reachable_when_skip = [0x0] * n
    for i in reversed(range(0, n - 1)):
        reachable_when_skip[i] = reachable_when_skip[i + 1] | connections[i + 1]

    reached = 0x0
    all_reached = 0x0
    for i in range(n):
        all_reached |= 1 << i 
    idx = 0
    best_count = float('inf')
    current_count = 0

    # precolor
    for v in range(n):
        # singleton and its not reached yet
        if nbits_set(connections[v], 1, n) and ((reached >> (n - 1 - v)) & 1) == 0:
            # color the vertex
            reached |= 1 << (n - 1) - v
            current_count += 1

        # leaf
        elif nbits_set(connections[v], 2, n):
            # find parent
            without_self = connections[v] & ~ (0x0 | (1 << (n - 1) - v))
            i = 0
            while i < n:
                if (without_self >> ((n - 1) - i)) & 1:
                    break
                i += 1
            # check that the parent is not reached yet
            if ((reached >> (n - 1 - i)) & 1) == 0:
                # color the ith vertex (parent of the leaf vertex)
                reached |= connections[i]
                current_count += 1

    min_count = stations_color(
        connections, 
        reachable_when_skip, 
        all_reached, 
        reached, 
        current_count, 
        best_count, 
        idx, 
        n
    )

    return min_count

if __name__ == "__main__":
    lines = [(int(num) for num in line.strip().split()) for line in sys.stdin.readlines() if line.strip() != '']

    it = 0
    while it < len(lines):
        n, m = lines[it]

        if n == 0 and m == 0:
            break

        # assert 3 <= n <= 35  # can use bitset

        connections = [0x0] * n

        for i in range(n):
            connections[i] |= 1 << (n - 1 - i)

        for i in range(it + 1, it + 1 + m): 
            u, v = lines[i]
            u -= 1
            v -= 1
            connections[u] |= 1 << (n - 1) - v  # set the v-th bit of number u
            connections[v] |= 1 << (n - 1) - u

        result = stations(connections)
        print(result)

        it += 1 + m
        
