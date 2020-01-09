def search(array, value):
    left = 1
    right = len(array)
    while left <= right:
        middle = (left + right) // 2
        middle_value = array[middle - 1]
        if middle_value == value:
            return middle
        if middle_value < value:
            left = middle + 1
        if value < middle_value:
            right = middle - 1
    return -1

def main():
    array = list(map(int, input().split(' ')))[1:]
    values = list(map(int, input().split(' ')))[1:]
    print(' '.join(map(lambda value: str(search(array, value)), values)))

if __name__ == "__main__":
    main()