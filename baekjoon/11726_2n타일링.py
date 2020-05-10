if __name__ == "__main__":
    n = int(input())

    arr = [0, 0, 1, 1]

    for i in range(4, n+1):
        x=y=z=987654321
        if i%3 == 0: x = arr[int(i/3)]
        if i%2 == 0: y = arr[int(i/2)]
        z = arr[i-1]
        
        arr.append(min(x,y,z)+1)
            
    print(arr[n])