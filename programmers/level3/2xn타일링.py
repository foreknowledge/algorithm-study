def solution(n):
    ans = [0, 1, 2]

    if n < 3: return ans[n]
    
    for i in range(3, n+1):
        ans.append((ans[i-2]+ans[i-1])%1000000007)

    return ans[n]


if __name__ == "__main__":
    print([solution(i) for i in range(10)])