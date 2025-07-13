import sys
from collections import deque, defaultdict

INF = 0xFFFF_FFFF_FFFF_FFFF

def merge_stepping(xs, step): 
    return [','.join(xs[i:i+step]).strip() for i in range(0, len(xs), step)]

def erdos(papers, queries):
    adj = defaultdict(list)
    numbering = {}  # keep track of numbering of authors: string: int

    author_chunks = [paper[:paper.find(':')].split(',') for paper in papers]
    # authors splitted up for each paper
    papers = [merge_stepping(name_chunks, 2) for name_chunks in author_chunks]

    source_author = 'Erdos, P.'
    source = None

    for authors in papers:
        A = len(authors)
        for i in range(A - 1):
            for j in range(i + 1, A):
                x, y = authors[i], authors[j]
                
                if x not in numbering:
                    numbering[x] = len(numbering)
                if y not in numbering:
                    numbering[y] = len(numbering)

                u, v = numbering[x], numbering[y]

                if x == source_author:
                    source = u
                elif y == source_author:
                    source = v

                adj[u].append(v)
                adj[v].append(u)
    
    if source is None:
        return [INF] * len(queries)
        
    V = len(numbering)
    dist = [INF] * V
    dist[source] = 0

    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == INF:
                dist[v] = dist[u] + 1
                queue.append(v)

    return [dist[numbering[q]] if q in numbering else INF for q in queries]

if __name__ == "__main__":
    data = [line.strip() for line in sys.stdin.readlines()]
    scenarios = int(data[0])

    i = 1
    k = 1
    while k <= scenarios:
        p, n = (int(x) for x in data[i].split())
        i += 1
        papers = [] 
        names = []
        for j in range(p):
            papers.append(data[i + j])
        i += p

        for j in range(n):
            names.append(data[i + j])
        i += n

        erdos_numbers = erdos(papers, names)
        print(f"Scenario {k}")

        for j in range(n):
            print(names[j], "infinity" if erdos_numbers[j] == INF else erdos_numbers[j])

        k += 1
