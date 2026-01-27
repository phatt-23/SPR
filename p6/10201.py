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

    # init dp (set all to INF)
    for pf in range(n):
        for j in range(tank_capacity + 1):
            dp[pf][j] = INF

    # we reach this station 0 because we start here
    dp[0][initial_fuel] = 0

    # check that the station 1 can be reached
    if dist[1] > initial_fuel:
        return None
    
    # we don't buy anything from the station 0 as it's the start and there is no station
    # the tank gets depleted by the distance to the station 1
    # we couldn't buy any fuel in station 0 (there's really no station 0)
    dp[1][initial_fuel - dist[1]] = 0
    
    # travel to next stations (2 until N - 1)
    for s in range(2, n):
        dist_to_current = dist[s] - dist[s - 1]

        # the minimal amount of fuel we can have when arriving at this station
        fuel_min = max(initial_fuel - dist[s], 0)

        # the maximal amount of fuel that can be inside the tank when we reach this station s from the previous station s - 1
        # we traveled dist_to_current units to get here, so if we had full tank, we would burn dist_to_current liters
        # meaning the maximum amount of fuel inside the tank is tank_capacity - dist_to_current
        # fuel_max models how much fuel can there at most be inside the tank when we arrive at this station
        # when arriving at the last statoin, we don't have to consider cases where we have more fuel than 100 l, 
        # because we don't want to waste our money to buy more fuel than necessary 
        fuel_max = initial_fuel if s == n - 1 else tank_capacity - dist_to_current

        # the minimal amount of fuel we could have had in the tank when arriving into the previous station s - 1
        prev_fuel_min = max(initial_fuel - dist[s - 1], 0)

        # consider every amount of fuel we could have when arriving at this station s
        # the tank could have [fuel_min, fuel_max] amount of fuel
        # consider how much fuel we must have bought when we were in the previous station s - 1
        # to get to this station with f amount of fuel in the tank
        for f in range(fuel_min, fuel_max + 1):
            # find the minimum price for getting to this stations s 
            # with f amount of fuel in the tank
            # considering having to buy gas in the previous station s - 1 for the price in s - 1
            # and that in the station s - 1 could have started some pf amount of fuel
            min_price = INF

            # the amount of fuel we must have had in the tank when departing from the station s - 1
            # for us to secure having f amount of fuel in the tank when arriving at this station s
            # (capping with min(tank_capacity) is mostly probably not necessary here)
            prev_fuel_max = dist_to_current + f
            
            for pf in range(prev_fuel_min, prev_fuel_max + 1):
                # if getting to the previous station with pf amount of fuel in the tank wasn't possible
                # then having pf+1, pf+2, ..., pf+n in the tank was also not possible
                if dp[s - 1][pf] == INF:
                    break

                # amount of fuel we must have bought in the previous station s - 1 whilst having pf amount of fuel in the tank
                # for us to have f amount of fuel when arriving at this station s
                bought_liters = prev_fuel_max - pf

                # if the current amount of fuel pf + amount we must bought exceeds the tank capacity, skip it
                if pf + bought_liters > tank_capacity:
                    break

                # the price to get here having pf amount of fuel in the tank in the previous station s - 1
                # and having to buy bought_liters of fuel for the price of station s - 1
                # (get the price from the previous travel + the price of the gas bought in the previous station to get here)
                candidate_price = dp[s - 1][pf] + price[s - 1] * bought_liters

                # update
                min_price = min(min_price, candidate_price)

            # if there's no way to get to the station s with f amount of fuel
            # then we can't go any further
            if min_price == INF:
                return None

            # assign the minimum found price
            # the cheapest way to get to the station s with f amount of fuel
            dp[s][f] = min_price  

    # print_dp(dp, n)

    # what's the cheapest price to get to the final station n - 1, having 100 or more litres of fuel in the tank
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

            # print('dist', dist)
            # print('price', price)

            result = moving(i)
            if result is None:
                print("Impossible")
            else:
                print(result)

            if idx + 1 < n and cases != -1:
                print()

        idx += 1
