import sys


def bitLen(num):
    length = 0
    while num:
        num >>= 1
        length += 1
    return length


def reconstruct(prev: list[list[int]], room, light, depth = 0):
    if room == 0 and light == 1:
        print(f"The problem can be solved in {depth} steps:")
        return
    else:
        value = prev[room][light]

        # if the value has the room's bit set, then it means switch was used
        if value & (1 << room):
            switch = value ^ (1 << room)
            prev_light = light ^ switch
            reconstruct(prev, room, prev_light, depth + 1)

            if light & switch:
                print(f"- Switch on light in room {bitLen(switch)}.")
            else:
                print(f"- Switch off light in room {bitLen(switch)}.")
        # else we got here by coming from neighboring room
        else:
            # if not then we got here from the 'value's bit room
            reconstruct(prev, bitLen(value) - 1, light, depth + 1)
            print(f"- Move to room {room + 1}.")


def solve(villa: list[list[int]], lights: list[list[int]]):
    room_count = len(villa)

    visited = [[False] * 2 ** room_count for _ in range(room_count)]
    prev = [[-1] * 2 ** room_count for _ in range(room_count)]

    Q = [(0, 1)]  # room 0 = hallway with lights on
    light = 1

    while len(Q) != 0:
        room, light = Q.pop(0)

        if visited[room][light]:
            continue
        else:
            visited[room][light] = True

        for switch, is_present in enumerate(lights[room]):
            if is_present:
                # must not turn off the lights of the current room
                if switch == room:
                    continue

                next_light = light ^ (1 << switch)

                if not visited[room][next_light]:
                    Q.append( (room, next_light) )
                    # im standing in this room and switched on the light
                    if prev[room][next_light] == -1:
                        # how do i know if im standing in room (1 << room) and switching (1 << switch) or standing in (1 << switch) and turn on (1 << room)??
                        prev[room][next_light] = (1 << room) | (1 << switch)  

        for next_room, is_connected in enumerate(villa[room]):
            if is_connected:
                # the next room is lit and it hasnt been visited with this light state yet
                if (light & (1 << next_room)) and not visited[next_room][light]:
                    Q.append( (next_room, light) )
                    # got to this room by coming from (1 << room)
                    if prev[next_room][light] == -1:
                        prev[next_room][light] = 1 << room
                
    return prev


if __name__ == "__main__":
    data = [int(a) for a in sys.stdin.read().split()]
    # print(data)

    idx = 0
    case = 1

    while True:
        rooms, doors, switches = data[idx], data[idx + 1], data[idx + 2]
        if rooms == doors == switches == 0: break
        assert rooms <= 10
        
        villa, lights = [[0] * rooms for _ in range(rooms)], [[0] * rooms for _ in range(rooms)]

        idx += 3
        for _ in range(doors):
            room_i, room_j = data[idx] - 1, data[idx + 1] - 1
            villa[room_i][room_j] = 1
            villa[room_j][room_i] = 1
            idx += 2

        for _ in range(switches):
            switch_k, light_l = data[idx] - 1, data[idx + 1] - 1
            lights[switch_k][light_l] = 1
            idx += 2

        print(f"Villa #{case}")

        prev = solve(villa, lights)

        bedroom = rooms - 1
        only_bedroom_light = 1 << bedroom
        if prev[bedroom][only_bedroom_light] != -1 or len(villa) == 1:
            reconstruct(prev, bedroom, only_bedroom_light)
        else:
            print("The problem cannot be solved.")

        print()
        case += 1

