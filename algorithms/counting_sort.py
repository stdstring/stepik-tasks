def main():
    max_value = 10
    n = int(input())
    numbers = list(map(lambda number: int(number), input().split(' ')))
    b = [0] * max_value
    for number in numbers:
        b[number - 1] += 1
    for index in range(1, max_value):
        b[index] += b[index - 1]
    result = [0] * n
    for index in range(n - 1, -1, -1):
        result[b[numbers[index] - 1] - 1] = numbers[index]
        b[numbers[index] - 1] -= 1
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()