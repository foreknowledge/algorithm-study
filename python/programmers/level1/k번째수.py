def solution(array, commands):
    ans = []
    for c in commands:
        a = array[c[0]-1:c[1]].sort()
        a.sort()
        ans.append(a[c[2]-1])
    
    return ans


if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))