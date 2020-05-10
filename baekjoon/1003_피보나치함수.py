if __name__ == "__main__":
    tc = int(input())

    while(tc > 0):
        tc -= 1
        
        arr = [[1, 0], [0, 1]]
        n = int(input())
        
        for i in range(2, n+1):
            arr.append([arr[i-1][0]+arr[i-2][0], arr[i-1][1]+arr[i-2][1]])
        
        print(arr[n][0], arr[n][1])