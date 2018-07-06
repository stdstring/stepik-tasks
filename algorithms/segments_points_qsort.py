def select_supporting_element(data, left, right):
    left_value = data[left]
    right_value = data[right]
    middle = (right + left) // 2
    middle_value = data[middle]
    if (left_value < middle_value) and (middle_value < right_value):
        return middle
    if (left_value < right_value) and (right_value < middle_value):
        return right
    if (middle_value < left_value) and (left_value < right_value):
        return left
    if (middle_value < right_value) and (right_value < left_value):
        return right
    if (right_value < left_value) and (left_value < middle_value):
        return left
    if (right_value < middle_value) and (middle_value < left_value):
        return middle
    if left_value == middle_value:
        return left
    if left_value == right_value:
        return left
    if middle_value == right_value:
        return middle
    return middle

def partition(data, left, right):
    supporting_element_index = select_supporting_element(data, left, right)
    supporting_element = data[supporting_element_index]
    data[supporting_element_index] = data[left]
    data[left] = supporting_element
    equal_part_start = left + 1
    greater_part_start = left + 1
    for index in range(left + 1, right + 1):
        current = data[index]
        if current < supporting_element:
            data[index] = data[greater_part_start]
            data[greater_part_start] = data[equal_part_start]
            data[equal_part_start] = current
            equal_part_start += 1
            greater_part_start += 1
        elif current == supporting_element:
            data[index] = data[greater_part_start]
            data[greater_part_start] = current
            greater_part_start += 1
        else:
            pass
    if equal_part_start > (left + 1):
        pass
    data[left] = data[equal_part_start - 1]
    data[equal_part_start - 1] = supporting_element
    equal_part_start -= 1
    return (equal_part_start, greater_part_start)

# left - first, right - last
def qsort(data, left, right):
    while (right - left) > 1:
        equal_part_start, greater_part_start = partition(data, left, right)
        less_part_size = equal_part_start - left
        greater_part_size = right - greater_part_start + 1
        if less_part_size < greater_part_size:
            # less_part_size may be equal 0
            qsort(data, left, equal_part_start - 1)
            left = greater_part_start
        else:
            # greater_part_size may be equal 0
            qsort(data, greater_part_start, right)
            right = equal_part_start - 1
    if ((right - left) == 1) and (data[left] > data[right]):
        element = data[left]
        data[left] = data[right]
        data[right] = element

def calculate_segment_count(segments_left, segments_right, point):
    from bisect import bisect_left
    left_count = bisect_left(segments_left, point + 1)
    right_count = bisect_left(segments_right, point)
    return left_count - right_count

def main():
    n, m = map(int, input().split())
    segments_left = []
    segments_right = []
    for _ in range(n):
        segment_left, segment_right = map(int, input().split())
        segments_left.append(segment_left)
        segments_right.append(segment_right)
    points = list(map(lambda number: int(number), input().split(' ')))
    qsort(segments_left, 0, n - 1)
    qsort(segments_right, 0, n - 1)
    segments_count = map(lambda point: calculate_segment_count(segments_left, segments_right, point), points)
    print(' '.join(map(lambda count: str(count), segments_count)))

if __name__ == "__main__":
    main()