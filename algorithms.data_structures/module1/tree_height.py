def process() -> None:
    n = int(input())
    parents = map(int, input().split())
    nodes_children = [[] for i in range(n)]
    root = -1
    for node, parent in enumerate(parents):
        if parent == -1:
            root = node
        else:
            nodes_children[parent].append(node)
    node_heights = [0] * n
    stack = [root]
    while len(stack) > 0:
        current = stack[-1]
        current_children = nodes_children[current]
        if len(current_children) == 0:
            node_heights[current] = 1
            stack.pop()
        elif node_heights[current_children[0]] > 0:
            node_heights[current] = max(map(lambda child: node_heights[child], current_children)) + 1
            stack.pop()
        else:
            stack.extend(current_children)
    print(node_heights[root])


if __name__ == "__main__":
    process()