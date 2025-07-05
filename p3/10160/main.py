import sys

def load_num():
    return int(sys.stdin.readline())

def load_line():
    return sys.stdin.readline()

def parse_ints(line):
    return list(map(int, line.split()))

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

if __name__ == "__main__":
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip() != '']

    i = 0
    while i < len(lines):
        n_vertices, m_edges = parse_ints(lines[i])
        i += 1

        if n_vertices == m_edges == 0:
            break
        
        graph = [[] for _ in range(n_vertices)]

        for line in lines[i:i + m_edges]:
            u, v = parse_ints(line)
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)

        i += m_edges

        result = stations(graph)
        print(result)

