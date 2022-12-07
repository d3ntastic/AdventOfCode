import os
import itertools

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        lines = f.read().splitlines()
    instructions = [
        [line.split(" ")[0]] + [list(range(int(part.split("=")[1].split("..")[0]), int(part.split("=")[1].split("..")[1]) + 1)) for part in line.split(",")] for line in lines]
    return instructions

def get_subrange(crange, low, high):
    c0 = crange[0]
    c1 = crange[-1]
    if c1 < low:
        return []
    elif c0 > high:
        return []
    c0 = max(c0, low)
    c1 = max(c1, low)
    c0 = min(c0, high)
    c1 = min(c1, high)
    return range(c0, c1+1)

def count_uninterrupted(item, rest):
    _, xr, yr, zr = item
    total = len(xr) * len(yr) * len(zr)

    conflicts = []
    ref_val = 0

    for idx, item in enumerate(rest):
        state, xr2, yr2, zr2 = item

        cxr = get_subrange(xr2, xr[0], xr[-1])
        cyr = get_subrange(yr2, yr[0], yr[-1])
        czr = get_subrange(zr2, zr[0], zr[-1])

        if len(cxr) == 0 or len(cyr) == 0 or len(czr) == 0:
            continue

        conflicts.append((state, cxr, cyr, czr))
        ref_val += len(cxr) * len(cyr) * len(czr)

    for idx, item in enumerate(conflicts):
        total -= count_uninterrupted(item, conflicts[idx+1:])

    return total

def get_activated_cubes(instructions, part_one = False):
    active_cubes = 0
    for idx, instruction in enumerate(instructions):
        state, x, y, z = instruction
        if part_one:
            if x[0] > 50 or x[-1] < -50 or y[0] > 50 or y[-1] < -50 or z[0] > 50 or z[-1] < -50:
                continue
        if (state == "off"):
            continue
        active_cubes += count_uninterrupted(instruction, instructions[idx+1:])
        
    return active_cubes

def part_one():
    instructions = read_input('./input.txt')
    activated_cubes = get_activated_cubes(instructions, True)
    return activated_cubes

def part_two():
    instructions = read_input('./input.txt')
    activated_cubes = get_activated_cubes(instructions, False)
    return activated_cubes

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()