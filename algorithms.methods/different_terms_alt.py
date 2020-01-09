import math

def main():
    n = int(input())
    arith_count = int((-1 + math.sqrt(1 + 8 * n)) / 2)
    print (arith_count)
    print (' '.join(map(str, range(1, arith_count))) + ' ' + str(n - (arith_count - 1) * arith_count // 2))

if __name__ == "__main__":
    main()