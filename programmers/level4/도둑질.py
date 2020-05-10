# -*- coding: utf-8 -*-

def solution(money):
    # 첫 번째 집을 터는 경우
    house1 = [money[0], money[0]]
    for i in range(2,len(money)-1):
        house1.append(max(house1[i-1], house1[i-2]+money[i]))
    
    # 첫 번째 집을 털지 않는 경우
    house2 = [0, money[1]]
    for i in range(2, len(money)):
        house2.append(max(house2[i-1], house2[i-2]+money[i]))

    return max(house1[-1], house2[-1])


if __name__ == "__main__":
    print(solution([1,2,3,1]))
    print(solution([1,2,3,1,5]))