import re
import sys


def hash_algorithm(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def main():
    # Fun fact: dicts in Python preserve insertion order!
    instruction_sequence = sys.stdin.readline().strip().split(",")
    boxes = [dict() for _ in range(256)]
    for instruction in instruction_sequence:
        label, focal_length = re.fullmatch(
            r"([a-z]+)(?:-|(?:=(\d)))", instruction
        ).groups()
        box = boxes[hash_algorithm(label)]
        if focal_length is not None:
            box[label] = int(focal_length)
        else:
            if label in box:
                del box[label]
    s = 0
    for i, box in enumerate(boxes):
        for j, focal_length in enumerate(box.values()):
            s += (i + 1) * (j + 1) * focal_length
    print(s)


if __name__ == "__main__":
    main()
