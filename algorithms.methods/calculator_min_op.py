def main():
    n = int(input())
    d = [0]
    for number in range(2, n + 1):
        # x + 1
        value = d[-1] + 1
        # 2x
        if number % 2 == 0:
            value = min(value, d[(number // 2) - 1] + 1)
        # 3x
        if number % 3 == 0:
            value = min(value, d[(number // 3) - 1] + 1)
        d.append(value)
    print(d[-1])
    solution = [n]
    number = n
    result = d[-1]
    while number > 1:
        if (number % 2 == 0) and (d[(number // 2) - 1] == result - 1):
            number //= 2
            result -= 1
        elif (number % 3 == 0) and (d[(number // 3) - 1] == result - 1):
            number //= 3
            result -= 1
        else:
            number -= 1
            result -= 1
        solution.append(number)
    solution.reverse()
    print(' '.join(map(str, solution)))

if __name__ == "__main__":
    main()