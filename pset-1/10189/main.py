import sys

kernel = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1), (1, 0), (1, 1),
)

if __name__ == "__main__":
    lines: list[str] = [line.strip() for line in sys.stdin.readlines()]

    i = 0
    field_cnt = 0
    outputs = []

    while i < len(lines):
        dimx, dimy = list(map(lambda x: int(x), lines[i].split()))

        if dimx == 0 and dimy == 0:
            break

        i += 1
        field_cnt += 1
        field = []

        for x in range(i,i+dimx):
            line = lines[x]
            field_line = []
            for y, punkt in enumerate(line):
                if punkt == '*': 
                    field_line.append('*')
                    continue

                bombs = 0
                for kx, ky in kernel:
                    nx = x + kx
                    ny = y + ky
                    
                    if i <= nx < i + dimx and 0 <= ny < dimy:
                        if lines[nx][ny] == '*':
                            bombs += 1

                field_line.append(str(bombs))
            field.append("".join(field_line))

        outputs.append(f"Field #{field_cnt}:\n" + "\n".join(field))
        i += dimx

    print("\n\n".join(outputs))
