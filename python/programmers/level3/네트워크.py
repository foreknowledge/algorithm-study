import queue

def solution(n, computers):
    nonVisited = [i for i in range(n)]
    q = queue.Queue()
    cnt = 0

    while nonVisited:
        q.put(nonVisited[0])
        cnt += 1
        
        while not q.empty():
            a = q.get()
            if a in nonVisited:
                nonVisited.remove(a)
                li = computers[a]
                for i in range(n):
                    if i in nonVisited and li[i] == 1:
                        q.put(i)

    return cnt
    

if __name__ == "__main__":
    n=3
    computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    
    print(solution(n,computers))