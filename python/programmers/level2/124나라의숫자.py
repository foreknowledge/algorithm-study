def solution(n):
    n -= 1
    m = n//3
    l = n%3

    if l==0: l=1
    elif l==1: l=2
    else: l=4

    if m==0: return str(l)
    elif 1<=m<3: return str(m)+str(l)
    elif m==3: return str(m+1)+str(l)
    else: return str(solution(m))+str(l)


if __name__ == "__main__":
    print(solution(500000000))