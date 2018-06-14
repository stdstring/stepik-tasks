from io import StringIO

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Leaf:
    def __init__(self, value):
        self.value = value

def extract_min(storage):
    min_index = 0
    _, min_count = storage[0]
    for index in range(1, len(storage)):
        _, count = storage[index]
        if count < min_count:
            min_count = count
            min_index = index
    return storage.pop(min_index)

def build_tree(storage):
    while len(storage) > 1:
        element1, count1 = extract_min(storage)
        element2, count2 = extract_min(storage)
        if (count1 == count2) and isinstance(element1, Leaf) and isinstance(element2, Node):
            element_left, element_right = element1, element2
        elif (count1 == count2) and isinstance(element1, Leaf) and isinstance(element2, Leaf):
            element_left, element_right = (element1, element2) if element1.value < element2.value else (element2, element1)
        else:
            element_left, element_right = element2, element1
        node = Node(element_left, element_right)
        storage.append((node, count1 + count2))
    return storage[0][0]

def build_encoding_table_impl(node, path, storage):
    if isinstance(node.left, Leaf):
        storage[node.left.value] = path + '0'
    else:
        build_encoding_table_impl(node.left, path + '0', storage)
    if isinstance(node.right, Leaf):
        storage[node.right.value] = path + '1'
    else:
        build_encoding_table_impl(node.right, path + '1', storage)

def build_encoding_table(tree):
    if isinstance(tree, Leaf):
        return {tree.value: '0'}
    else:
        storage = {}
        build_encoding_table_impl(tree, '', storage)
        return storage

def encode_str(source, table):
    buffer = StringIO()
    for ch in source:
        buffer.write(table[ch])
    return buffer.getvalue()

def get_encoding_table_repr(encoding_table):
    encoding_table = list(encoding_table.items())
    encoding_table.sort(key=lambda item: item[0])
    return '\r\n'.join(map(lambda item: '{0}: {1}'.format(item[0], item[1]), encoding_table))

def main():
    source = input()
    storage = {}
    for ch in source:
        count = storage[ch] if ch in storage else 0
        storage[ch] = count + 1
    tree = build_tree(list(map(lambda pair : (Leaf(pair[0]), pair[1]), storage.items())))
    encoding_table = build_encoding_table(tree)
    dest = encode_str(source, encoding_table)
    print ('{0} {1}'.format(len(storage), len(dest)))
    print (get_encoding_table_repr(encoding_table))
    print (dest)

if __name__ == "__main__":
    main()