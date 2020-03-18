import collections


def process() -> None:
    q = int(input())
    number_stack = collections.deque()
    max_stack = collections.deque()
    for _ in range(q):
        command = input().split()
        if command[0] == "push":
            value = int(command[1])
            number_stack.append(value)
            max_stack.append(value if len(max_stack) == 0 else max(value, max_stack[-1]))
        elif command[0] == "pop":
            number_stack.pop()
            max_stack.pop()
        elif command[0] == "max":
            print(max_stack[-1])


if __name__ == "__main__":
    process()