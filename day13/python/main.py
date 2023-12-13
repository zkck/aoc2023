from collections import defaultdict
import sys


def rotate_left(pattern: list[str]):
    return [
        "".join(pattern[i][j] for i in range(len(pattern)))
        for j in reversed(range(len(pattern[0])))
    ]


def find_splits(line: str):
    for i in range(1, len(line)):
        if all(c1 == c2 for (c1, c2) in zip(reversed(line[:i]), line[i:])):
            yield i


def find_vertical_line(pattern: list[str]) -> int:
    split_counters = defaultdict(int)
    for line in pattern:
        for split in find_splits(line):
            split_counters[split] += 1
    for split, count in split_counters.items():
        if count == len(pattern):
            return split
    # invalid result
    return 0


def main():
    lines = sys.stdin.read().splitlines()
    lines.append("")
    s = 0
    current_pattern = []
    for line in lines:
        if line:
            current_pattern.append(line)
        else:
            result = find_vertical_line(current_pattern)
            if result:
                s += result
            else:
                s += 100 * find_vertical_line(rotate_left(current_pattern))
            current_pattern = []

    print(s)

if __name__ == "__main__":
    main()
