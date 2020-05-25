import math

def solution(progresses, speeds):
    work = []
    for i in range(len(progresses)):
        progress = int(progresses[i])
        speed = int(speeds[i])

        work.append(math.ceil((100-progress)/speed))

    release = []
    current = work[0]
    cnt = 1
    for i in range(1, len(work)):
        if work[i] <= current: 
            cnt += 1
        else:
            release.append(cnt)
            current = work[i]
            cnt = 1
    
    release.append(cnt)

    return release

if __name__ == "__main__":
    print(solution([93,30,55], [1,30,5]))
    print(solution([93,30,55], [1,30,10]))
    print(solution([93,30,55,44], [1,30,5,15]))
    print(solution([50,50,50,50,50], [10,10,15,20,30]))