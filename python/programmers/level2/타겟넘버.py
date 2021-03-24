import queue

def solution(numbers, target):
    q=queue.Queue()
    q.put((numbers[0],0))
    q.put(((-1)*numbers[0],0))
    cnt = 0

    while not q.empty():
        n, i = q.get()
        if (i+1<len(numbers)):
            q.put((n+numbers[i+1],i+1))
            q.put((n-numbers[i+1],i+1))
        elif (n == target):
            cnt += 1
    
    return cnt
        

if __name__ == "__main__":
    n=[1,1,1,1,1]
    t=3
    print(solution(n,t))