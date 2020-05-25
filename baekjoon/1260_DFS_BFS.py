import collections as c

def dfs(v, graph):
    stack = [v]
    visited = set()

    while stack:
        a = stack.pop()

        if a not in visited:
            print(a, end = " ")
            visited.add(a)

            if graph.get(a):
                stack.extend(sorted(graph[a], reverse=True))
    print()

def bfs(v, graph):
    queue = c.deque()
    queue.append(v)
    visited = set()

    while queue:
        a = queue.popleft()

        if a not in visited:
            print(a, end=" ")
            visited.add(a)

            if graph.get(a):
                [queue.append(i) for i in sorted(graph[a])]
    print()

if __name__ == "__main__":
    n, m, v = map(int, input().split())
    graph = {}

    for i in range(m):
        a, b = map(int, input().split())
        if graph.get(a):
            t = graph[a]
            t.append(b)
            graph[a] = t
        else:
            graph[a] = [b]

        if graph.get(b):
            t = graph[b]
            t.append(a)
            graph[b] = t
        else:
            graph[b] = [a]

    dfs(v, graph)
    bfs(v, graph)