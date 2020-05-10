# -*- coding: utf-8 -*-
import queue

def solution(begin, target, words):
    graph = [[0]*(len(words)+1) for _ in range(len(words)+1)]

    # begin 인접행렬 그래프 만들기
    for i in range(len(words)):
        if diff_one(begin, words[i]):
            graph[0][i+1] = 1
            graph[i+1][0] = 1

    # words 인접행렬 그래프 만들기
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if diff_one(words[i], words[j]):
                graph[i+1][j+1] = 1
                graph[j+1][i+1] = 1

    return bfs(graph, target, words)

def bfs(graph, target, words):
    q = queue.Queue()
    checked = [0] * (len(words)+1)
    q.put([0, 0])
    checked[0] = 1

    while not q.empty():
        index, depth = q.get()
        for i in range(len(graph[index])):
            if graph[index][i] == 1 and checked[i] == 0:
                if words[i-1]==target: return depth+1
                q.put([i, depth+1])
                checked[i] = 1
    
    return 0

def diff_one(word1, word2):
    diff_cnt = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]: 
            diff_cnt += 1
    
    if diff_cnt == 1: return True
    else: return False
        

if __name__ == "__main__":
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))