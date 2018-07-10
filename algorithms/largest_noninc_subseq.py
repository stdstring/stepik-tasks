import bisect
import math

def main():
    n = int(input())
    numbers = list(map(lambda number: -1 * int(number), input().split(' ')))
    d = [math.inf] * (n + 1)
    d[0] = -math.inf
    pos = [-1] * (n + 1)
    prev = [-1] * (n + 1)
    length = 0
    for index in range(n):
        number = numbers[index]
        j = bisect.bisect_right(d, number)
        if (d[j-1] <= number) and (number <= d[j]):
            d[j] = number
            pos[j] = index + 1
            prev[index] = pos[j - 1]
            length = max(length, j)
    answer = []
    index = pos[length]
    while index != -1:
        answer.append(index)
        index = prev[index - 1]
    answer.reverse()
    print(len(answer))
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    main()