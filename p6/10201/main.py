import sys

INF = 0xFFFF_FFFF_FFFF_FFFF
tank_capacity = 200
initial_fuel = 100
max_stations = 100 + 2
dp = [[INF] * (tank_capacity + 1) for _ in range(max_stations)]
dist = [0] * max_stations
price = [0] * max_stations

def print_dp(dp, n):
    for i in range(n):
        print([v if v != INF else '-' for v in dp[i]])

def moving(n):
    assert n <= max_stations

    # init dp
    for i in range(n):
        for j in range(tank_capacity + 1):
            dp[i][j] = INF

    dp[0][initial_fuel] = 0

    # check that the first station can be reached
    if dist[1] - dist[0] > initial_fuel:
        return None
    dp[1][initial_fuel - dist[1] - dist[0]] = 0
    
    for s in range(2, n):
        dist_to_prev = dist[s] - dist[s - 1]

        if s == n - 1:
            fuel_end = initial_fuel
        else:
            fuel_end = tank_capacity - dist_to_prev
       
        fuel_start = max(initial_fuel - dist[s], 0)

        # for other stations
        for f in range(fuel_start, fuel_end + 1):
            # find the minimum value of how to get to this stations s with f amount of fuel
            # considering having to buy gas in the previous station
            min_price = INF

            prev_start = max(initial_fuel - dist[s - 1], 0)
            prev_end = min(f + dist_to_prev + 1, tank_capacity + 1)
            
            for i in range(prev_start, prev_end):
                # if getting to the previous station 
                # with i amount of fuel wasn't possible, skip it
                if dp[s - 1][i] == INF:
                    break

                must_buy = f + dist_to_prev - i  # amount of fuel we must have bought in the previous station

                # if the current amount of fuel i + amount we must buy exceeds the tank capacity, skip it
                if i + must_buy > tank_capacity:
                    break

                # get the price from the previous travel + the price of the gas bought in the previous station to get here
                candidate_price = dp[s - 1][i] + price[s - 1] * must_buy

                min_price = min(min_price, candidate_price)

            if min_price == INF:
                return None

            dp[s][f] = min_price  # assign the minimum found price


    # print_dp(dp, n)

    # at the destination, with 100 litres of fuel or more
    min_cost = min(dp[n - 1][initial_fuel:])
    return min_cost if min_cost != INF else None

if __name__ == "__main__":
    data = list(map(str.strip, sys.stdin.readlines()))
    n = len(data)
    idx = 0
    cases = int(data[idx])
    idx += 1
    while idx < n and cases != -1:
        if data[idx] == '':
            cases -= 1
        else:
            dest_dist = int(data[idx])
            idx += 1

            i = 0
            dist[i] = 0
            price[i] = INF
            i += 1

            while idx < n and data[idx] != '':
                d, p = list(map(int, data[idx].split()))
                if d < dest_dist:
                    dist[i] = d
                    price[i] = p
                    i += 1
                idx += 1

            dist[i] = dest_dist
            price[i] = INF
            i += 1

            result = moving(i)
            if result is None:
                print("Impossible")
            else:
                print(result)

            if idx + 1 < n and cases != -1:
                print()

        idx += 1
