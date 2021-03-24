def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    visited = set()
    visited.add(0)

    while len(visited) < n:
        for s, e, c in costs:
            if s in visited or e in visited:
                if s in visited and e in visited: continue
                visited.add(s)
                visited.add(e)
                answer += c
                break

    return answer


if __name__ == "__main__":
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))