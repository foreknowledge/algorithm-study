def solution(scores):
    target = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))

    count = 0
    max_b = 0
    for s in scores:
        if target[0] < s[0] and target[1] < s[1]:
            return -1
        if max_b <= s[1]:
            if sum(target) < sum(s):
                count += 1
            max_b = s[1]

    return count+1


print(solution([[5, 7], [10, 3], [5, 6], [5, 2], [6, 7], [6, 4]]))
