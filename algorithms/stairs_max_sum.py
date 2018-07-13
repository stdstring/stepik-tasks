def main():
    n = int(input())
    numbers = list(map(int, input().split(' ')))
    prev = 0
    current = 0
    for number in numbers:
        next = max(number + current, number + prev)
        prev, current = current, next
    print(next)

if __name__ == "__main__":
    main()