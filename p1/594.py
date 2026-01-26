import sys

if __name__ == "__main__":
    numbers = [int(line.strip()) for line in sys.stdin.readlines()]

    for number in numbers:
        b1 = number        & 0xFF
        b2 = number >>   8 & 0xFF
        b3 = number >> 2*8 & 0xFF
        b4 = number >> 3*8 & 0xFF

        swapped = b1 << 3*8 | b2 << 2*8 | b3 << 8 | b4 

        if swapped & (0x1 << 31):
            swapped = -(1 + (swapped ^ 0xFFFFFFFF))
        print(number, "converts to", swapped)
