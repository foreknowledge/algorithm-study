if __name__ == "__main__":
    n = int(input())
    li = list(map(int, input().split()))
    arr = [[li[0],1]]
    _max_ = 1

    for i in range(1, n):
        candidates = []
        [candidates.append(e) for e in arr if e[0] < li[i]]
        
        max_cnt = 0
        for c in candidates :
            if c[1] > max_cnt:
                max_cnt = c[1]
        arr.append([li[i], max_cnt+1])
        
        if max_cnt+1 > _max_: _max_ = max_cnt+1

    print(_max_)