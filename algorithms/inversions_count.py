import array

def merge(numbers, buffer, first_start, second_start, portion_size, inversion_count):
    first_end = first_start + portion_size
    second_end = second_start + portion_size
    if second_end >= len(numbers):
        second_end = len(numbers)
    first_index = first_start
    second_index = second_start
    buffer_index = first_index
    while (first_index < first_end) and (second_index < second_end):
        if numbers[first_index] <= numbers[second_index]:
            buffer[buffer_index] = numbers[first_index]
            first_index += 1
            buffer_index += 1
        else:
            buffer[buffer_index] = numbers[second_index]
            inversion_count += (first_end - first_index)
            second_index += 1
            buffer_index += 1
    while first_index < first_end:
        buffer[buffer_index] = numbers[first_index]
        first_index += 1
        buffer_index += 1
    while second_index < second_end:
        buffer[buffer_index] = numbers[second_index]
        second_index += 1
        buffer_index += 1
    return inversion_count

def copy_numbers(numbers, buffer, start):
    index = start
    while index < len(numbers):
        buffer[index] = numbers[index]
        index += 1

def process_portions(numbers, buffer, portion_size, inversion_count):
    first_start = 0
    second_start = portion_size
    while second_start < len(numbers):
        inversion_count = merge(numbers, buffer, first_start, second_start, portion_size, inversion_count)
        first_start += 2 * portion_size
        second_start += 2 * portion_size
    copy_numbers(numbers, buffer, first_start)
    return inversion_count

def main():
    n = int(input())
    numbers = list(map(lambda number: int(number), input().split(' ')))
    numbers = array.array('L', numbers)
    buffer = array.array('L', [0] * len(numbers))
    portion_size = 1
    inversion_count = 0
    while portion_size < len(numbers):
        inversion_count = process_portions(numbers, buffer, portion_size, inversion_count)
        numbers, buffer = buffer, numbers
        portion_size *= 2
    print(inversion_count)

if __name__ == "__main__":
    main()