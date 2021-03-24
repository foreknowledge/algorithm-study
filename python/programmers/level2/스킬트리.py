import queue

def check(skill, skill_tree):
    q = queue.Queue()
    for i in skill: q.put(i)

    for i in skill_tree:
        if i in skill and q.get() != i: return 0

    return 1


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer += check(skill, skill_tree)

    return answer

if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(skill, skill_trees))