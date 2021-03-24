if __name__ == "__main__":
    N = int(input())

    T = [-1]
    P = [-1]
    for i in range(N):
        a = list(map(int, input().split()))
        T.append(a[0])
        P.append(a[1])

    arr = []
    _max_ = 0

    if T[1] <= N:
        arr.append([1+T[1], P[1]])
        if _max_ < P[1]: _max_ = P[1]
        
    for i in range(2, N+1):
        candidates = []
        [candidates.append(e) for e in arr if e[0] <= i] # 가능
        
        if len(candidates) == 0:  # 불가능
            if i+T[i] <= N+1:
                arr.append([i+T[i],P[i]])
                if _max_ < P[i]: _max_ = P[i]
        else:
            max_p = 0
            for c in candidates:
                if c[1] > max_p:
                    max_p = c[1]
            if i+T[i] <= N+1:
                arr.append([i+T[i], max_p+P[i]])
                if _max_ < max_p+P[i]: _max_ = max_p+P[i]
                
    print(_max_)