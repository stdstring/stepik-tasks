def main():
    w_max, n = map(int, input().split())
    weights = list(map(int, input().split(' ')))
    prev_row = []
    current_row = [0] * (w_max + 1)
    for number in range(1, n + 1):
        prev_row = current_row
        current_row = [0]
        for w in range(1, w_max + 1):
            value = prev_row[w]
            if weights[number - 1] <= w:
                value = max(prev_row[w - weights[number - 1]] + weights[number - 1], value)
            current_row.append(value)
    print(current_row[-1])

if __name__ == "__main__":
    main()