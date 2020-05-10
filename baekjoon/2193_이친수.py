if __name__ == "__main__":
    arr = [[0, 1], [1, 0]]
    n = int(input())

    for i in range(2, n):
        arr.append([arr[i-1][0]+arr[i-1][1], arr[i-1][0]])

    print(arr[n-1][0]+arr[n-1][1])