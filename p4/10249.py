import sys

read = sys.stdin.read

def dinner(team_members, table_caps):
    teams = [(i, [-1] * team_members[i]) for i in range(len(team_members))]
    teams = sorted(teams, key=lambda x: -len(x[1]))
    tables = [(i, table_caps[i]) for i in range(len(table_caps))]
    tables = sorted(tables, key=lambda x: -x[1])

    tm_indices = [0] * len(teams)
    for tb_ord, tb_cap in tables:
        for i in range(min(len(teams), tb_cap)):
            _, tm_arr = teams[i]
            if tm_indices[i] < len(tm_arr):
                tm_arr[tm_indices[i]] = tb_ord + 1
                tm_indices[i] += 1

    for _, tm_arr in teams:
        if -1 in tm_arr:
            return None

    return [i[1] for i in sorted(teams, key=lambda x: x[0])]


if __name__ == '__main__':
    data = list(map(int, read().split()))

    idx = 0
    while idx < len(data):
        team_count, table_count = data[idx], data[idx + 1]
        if team_count == 0 and table_count == 0:
            break
        idx += 2
        team_members = data[idx:idx + team_count]
        idx += team_count
        table_caps = data[idx:idx + table_count]
        idx += table_count

        team_sittings = dinner(team_members, table_caps)
        if team_sittings is None:
            print(0)
        else:
            print(1)
            for sitting in team_sittings:
                print(' '.join(map(str, sitting)))


    
