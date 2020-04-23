if __name__ == "__main__":
    storage_size = 10000000
    storage = [None for _ in range(storage_size)]
    n = int(input())
    for _ in range(n):
        request = input().split()
        method = request[0]
        number = int(request[1])
        if method == "add":
            storage[number] = request[2]
        elif method == "del":
            storage[number] = None
        elif method == "find":
            print("not found" if storage[number] is None else storage[number])
