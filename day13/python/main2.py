from collections import defaultdict
import sys


def count_mirror_violations(line: str, split: int):
    return sum(
        c1 != c2 for c1, c2 in zip(reversed(line[:split]), line[split:])
    )


def rotate_left(pattern: list[str]):
    return [
        "".join(pattern[i][j] for i in range(len(pattern)))
        for j in reversed(range(len(pattern[0])))
    ]


def find_splits(line: str):
    for i in range(1, len(line)):
        if not count_mirror_violations(line, i):
            # no violations, valid split
            yield i


def find_fixable_split(pattern: list[str]) -> int:
    split_counters = defaultdict(int)
    for line in pattern:
        for split in find_splits(line):
            split_counters[split] += 1

    for split, votes in split_counters.items():
        if votes == len(pattern) - 1:
            # split is just missing one vote.
            if (
                sum(count_mirror_violations(line, split) for line in pattern)
                == 1
            ):
                # split is singlularly fixable.
                return split

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
            split = find_fixable_split(current_pattern)
            if split:
                s += split
            else:
                s += 100 * find_fixable_split(rotate_left(current_pattern))
            current_pattern = []

    print(s)


if __name__ == "__main__":
    main()
