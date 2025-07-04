import sys

def load_num():
    return int(sys.stdin.readline())

def load_line():
    return sys.stdin.readline()

def parse_ints(line):
    return list(map(int, line.split()))

def stations(graph):
    
    
    
    return 0 

if __name__ == "__main__":
    n_vertices, m_edges = parse_ints(load_line())
    
    graph = [[] for _ in range(n_vertices)]

    for _ in range(m_edges):
        u, v = parse_ints(load_line())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    result = stations(graph)
    print(result)

