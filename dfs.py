graph = {
    '1': ['2', '3'],
    '2': ['4','5'],
    '3': ['5'],
    '4': ['1'],
    '5':['3']
}


def dfs(graph, node):
    visited = [node]
    stack = [node]
    print(node, end="->")
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.extend(node)
            print(node, end="->")
        remove_from_stack = True
        for next in graph[node]:
            if next not in visited:
                stack.extend(next)
                remove_from_stack = False
                break
        if remove_from_stack:
            stack.pop()
    return visited


print("Following is the Depth-First Search")
dfs(graph, '2')
