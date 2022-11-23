graph = {
    '1': ['2', '3'],
    '2': ['4','5'],
    '3': ['5'],
    '4': ['1'],
    '5':['3']
}


def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end="->")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("Following is the Breadth-First Search")
bfs(graph, '2')

print("\n")
