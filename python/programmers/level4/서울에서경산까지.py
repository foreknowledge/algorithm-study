def solution(K, travel):
    D = [{}]
    if travel[0][0] <= K:
        D[0] = {travel[0][0]:travel[0][1]}

    if travel[0][2] <= K:
        if travel[0][0] == travel[0][2]:
            D[0][travel[0][0]] = max(travel[0][1], travel[0][3])
        else:
            D[0][travel[0][2]] = travel[0][3]

    for i in range(1, len(travel)):
        D.append({})
        for time in D[i-1]:
            walk_time = time + travel[i][0]
            if walk_time <= K:
                if D[i].get(walk_time):
                    D[i][walk_time] = max(D[i][walk_time], D[i-1][time] + travel[i][1])
                else:
                    D[i][walk_time] = D[i-1][time] + travel[i][1]
            bike_time = time + travel[i][2]
            if bike_time <= K:
                if D[i].get(bike_time):
                    D[i][bike_time] = max(D[i][bike_time], D[i-1][time] + travel[i][3])
                else:
                    D[i][bike_time] = D[i-1][time] + travel[i][3]

    if len(D[len(travel)-1]) == 0: return 0
    return max(D[len(travel)-1].values())


if __name__ == "__main__":
    print(solution(1650, [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]))
    print(solution(3000, [[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]]))
