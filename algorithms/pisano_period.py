def try_calc_pisano_period(n, m):
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = [0, 1]
    prev = 0
    current = 1
    current_n = 1
    while (current_n < n):
        current_n += 1
        current, prev = (current + prev) % m, current
        if (result[-1] == 0) and (current == 1):
            return result[:-1]
        result.append(current)
    return current

def fib_mod(n, m):
    period_result = try_calc_pisano_period(n, m)
    return period_result[n % len(period_result)] if type(period_result) is list else period_result


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()