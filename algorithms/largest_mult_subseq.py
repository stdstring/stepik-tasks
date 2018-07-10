def main():
    n = int(input())
    numbers = list(map(lambda number: int(number), input().split(' ')))
    result = [0] * n
    for i in range(n):
        result[i] = 1
        for j in range(i):
            if (numbers[i] % numbers[j] == 0) and (result[i] < result[j] + 1):
                result[i] = result[j] + 1
    answer = 0
    for value in result:
        if value > answer:
            answer = value
    print(answer)

if __name__ == "__main__":
    main()