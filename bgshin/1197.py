# 그래프 탐색 기본 (하) - 최소 스페닝 트리

def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, x, y):
    root_x 
    = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1

def kruskal_algorithm(graph):
    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((weight, node, neighbor))

    edges.sort()

    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}

    mst = []

    for edge in edges:
        weight, src, dest = edge
        if find(parent, src) != find(parent, dest):
            mst.append(edge)
            union(parent, rank, src, dest)

    return mst

graph = {
    'A': [('B', 7), ('D', 5)],
    'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
    'C': [('B', 8), ('E', 5)],
    'D': [('A', 5), ('B', 9), ('E', 7), ('F', 6)],
    'E': [('B', 7), ('C', 5), ('D', 7), ('F', 8), ('G', 9)],
    'F': [('D', 6), ('E', 8), ('G', 11)],
    'G': [('E', 9), ('F', 11)]
}

mst = kruskal_algorithm(graph)
print("Edges in the minimum spanning tree are:", mst)