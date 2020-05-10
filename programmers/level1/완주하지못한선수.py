import collections

def solution1(participant, completion):
    ans = collections.Counter(participant) - collections.Counter(completion)
    return list(ans.keys())[0]

def solution2(participant, completion):
    answer = {}
    for c in completion:
        answer[c] = answer.get(c, 0) + 1

    for p in participant:
        if p not in answer or answer[p] == 0: return p
        answer[p] -= 1

def solution3(participant, completion):
    answer = {}
    for p in participant:
        answer[p] = answer.get(p, 0) + 1

    for c in completion: answer[c] -= 1

    print(answer.items())
    test = [k for k,v in answer.items() if v > 0]
    return test[0]

if __name__ == "__main__":
    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]

    print(solution1(participant, completion))
    print(solution2(participant, completion))
    print(solution3(participant, completion))