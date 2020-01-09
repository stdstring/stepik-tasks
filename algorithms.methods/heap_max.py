def get_parent_index(index):
    return index // 2

def get_children_indices(heap, index):
    left_child = 2 * index
    right_child = 2 * index + 1
    if len(heap) < left_child:
        return []
    return [left_child] if len(heap) < right_child else [left_child, right_child]

def insert(heap, number):
    heap.append(number)
    # shift up
    index = len(heap)
    while index > 1:
        parent_index = get_parent_index(index)
        if heap[parent_index - 1] > number:
            break
        heap[index - 1] = heap[parent_index - 1]
        heap[parent_index - 1] = number
        index = parent_index
    return heap

def extract_max(heap):
    if len(heap) == 1:
        print(heap.pop(0))
        return heap
    max = heap[0]
    last = heap.pop(-1)
    heap[0] = last
    # shift down
    index = 1
    finish = False
    while not finish:
        finish = True
        children = get_children_indices(heap, index)
        value = heap[index - 1]
        left_child_value = heap[children[0] - 1] if len(children) > 0 else value
        right_child_value = heap[children[1] - 1] if len(children) > 1 else value
        if value < left_child_value or value < right_child_value:
            child_index = children[0] if left_child_value >= right_child_value else children[1]
            heap[index - 1] = heap[child_index - 1]
            heap[child_index - 1] = last
            index = child_index
            finish = False
    print(max)
    return heap

def parse_command(command):
    if command == 'ExtractMax':
        return extract_max
    if command.startswith('Insert '):
        return lambda heap: insert(heap, int(command[len('Insert '):]))
    return lambda heap: heap

def main():
    n = int(input())
    commands = list(map(lambda _: input(),range(n)))
    heap = []
    for command in commands:
        heap = parse_command(command)(heap)

if __name__ == "__main__":
    main()