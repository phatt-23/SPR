import sys
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
        # case 1: skip
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
   
def nbit_set(seq, n, seq_len):
    ones = 0
    for i in range(seq_len):
        if seq >> i & 1 == 1:
            ones += 1
        if ones > n:
            return False
    return True

def stations(connections):
    n = len(connections)
    
    # if I skip node i, can I still reach every node?
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
        if nbit_set(connections[v], 1, n) and ((reached >> (n - 1 - v)) & 1) == 0:
            # color the vertex
            reached |= 1 << (n - 1) - v
            current_count += 1

        # leaf
        elif nbit_set(connections[v], 2, n):
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
            connections[u] |= 1 << (n - 1) - v
            connections[v] |= 1 << (n - 1) - u

        result = stations(connections)
        print(result)

        it += 1 + m
        
