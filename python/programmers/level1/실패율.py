def solution(N, stages):
    stage_dict = {}

    for s in stages:
        stage_dict[s] = stage_dict.get(s, 0) + 1

    rank = {}
    tot = len(stages)
    for i in range(1, N+1):
        if i in stage_dict and tot > 0:
            rank[i] = stage_dict[i]/tot
            tot -= stage_dict[i]
        else: rank[i] = 0

    return [k for k,v in sorted(rank.items(), key=lambda x: x[1], reverse=True)]

if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    print(solution(4, [4, 4, 4, 4, 4]))