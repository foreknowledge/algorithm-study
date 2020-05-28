import collections

def solution(begin, target, words):
    if target not in words: return 0

    graph = {}

    # begin 인접 리스트 만들기
    for w in words:
        if changable(begin, w):
            graph[begin] = graph.get(begin, []) + [w]

    # words 인접 리스트 만들기
    n = len(words)
    for i in range(n):
        for j in range(i, n):
            if changable(words[i], words[j]):
                graph[words[i]] = graph.get(words[i], []) + [words[j]]
                graph[words[j]] = graph.get(words[j], []) + [words[i]]

    return bfs(begin, target, graph)

def changable(target, source):
    diff = 0
    for i in range(len(target)):
        if target[i] != source[i]: diff += 1
    return diff == 1

def bfs(v, target, graph):
    queue = collections.deque()
    queue.append([v, 0])
    visited = set()

    while queue:
        a, depth = queue.popleft()

        if a in visited: continue
        if a == target: return depth

        visited.add(a)

        if graph.get(a):
            [queue.append([i, depth+1]) for i in sorted(graph[a])]

if __name__ == "__main__":
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))