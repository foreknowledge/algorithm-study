def solution(s):
    small=987654321

    for l in range(1,int(len(s)/2)+2):
        new = ""
        cnt = {}
        li = []
        result = ""
        start = 0
        for i in range(int(len(s)/l)+1):
            start = l*i
            n = s[start:l+start]
            if len(new) == 0:
                new += n
                cnt[n] = 1
            else:
                if new[-1*l:] == n:
                    a = cnt[n]
                    cnt[n] = a+1
                else:
                    li.append([new[-1*l:], cnt[new[-1*l:]]])
                    new += n
                    cnt[n] = 1
        li.append([s[start:], cnt[s[start:]]])

        for i in range(len(li)):
            if li[i][1] != 1:
                result += str(li[i][1]) + li[i][0]
            else:
                result += li[i][0]
        
        if small > len(result):
            small = len(result)
        
    return small
    

if __name__ == "__main__":
    print(solution("aabbaccc"))