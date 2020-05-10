def solution(p):
    if len(p) == 0: return p

    u = ""
    v = ""
    for i in range(1,len(p)):
        if isBalanced(p[0:i+1]): 
            u = p[0:i+1]
            v = p[i+1:]
            if isCorrect(u):
                return u + solution(v)
            else :
                new = "(" + solution(v) + ")"
                for i in u[1:-1]:
                    if i == '(':
                        new += ')'
                    else :
                        new += '('
                return new

def isCorrect(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False

    return len(stack) == 0

def isBalanced(p):
    return p.count('(') == p.count(')')


if __name__ == "__main__":
    p = ")("
    print(solution(p))
