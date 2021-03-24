def solution_recur(left, right):
    return recursive(left, right, 0, 0)

def recursive(left, right, l, r):
    if l == len(left) or r == len(right):
        return 0

    if left[l] > right[r]:
        return recursive(left, right, l, r+1) + right[r]
    else:
        return max(recursive(left, right, l+1, r), recursive(left, right, l+1, r+1))



def solution_memo(left, right):
    memo = [[-1]*len(left) for _ in range(len(right))]
    return memoization(memo, left, right, 0, 0)

def memoization(memo, left, right, l, r):
    if l == len(left) or r == len(right):
        return 0

    if memo[l][r] != -1: return memo[l][r]

    if left[l] > right[r]:
        ans = memoization(memo, left, right, l, r+1) + right[r]
        memo[l][r] = ans
        return ans
    else:
        ans = max(memoization(memo, left, right, l+1, r+1), memoization(memo, left, right, l+1, r))
        memo[l][r] = ans
        return ans



def bottomUp(left, right):
    dp = [[0]*(len(left)+1) for _ in range(len(right)+1)]
    
    for l in range(len(left)-1,-1,-1):
        for r in range(len(right)-1,-1,-1):
            if left[l] > right[r]: 
                dp[l][r] = dp[l][r+1] + right[r]
            else:
                dp[l][r] = max(dp[l+1][r+1], dp[l+1][r])

    return dp[0][0]
    
def bottomUp2(left, right):
    dp = [[0]*(len(left)+1) for _ in range(len(right)+1)]

    for i in range(1, len(left)+1):
        for j in range(1, len(right)+1):
            if left[i-1] > right[j-1]:
                dp[i][j] = dp[i][j-1] + right[j-1]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

    return dp[len(left)][len(right)]


if __name__ == "__main__":
    print(solution_recur([3,3,1],[7,7,1]))
    print(solution_memo([3,3,1],[7,7,1]))
    print(bottomUp([3,3,1],[7,7,1]))
    print(bottomUp2([3,3,1],[7,7,1]))
    print(bottomUp([1, 1, 9, 1, 1, 1, 1], [8, 9, 1, 1, 1, 1, 1]))
    print(bottomUp2([1, 1, 9, 1, 1, 1, 1], [8, 9, 1, 1, 1, 1, 1]))
