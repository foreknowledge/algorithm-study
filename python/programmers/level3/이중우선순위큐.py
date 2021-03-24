def solution(operations):
    queue = []

    for o in operations:
        operation, value = o.split()
        if operation == "I": 
            queue.append(int(value))
        elif operation == "D":
            if value == "1" and len(queue) != 0:
                queue.remove(max(queue))
            elif value == "-1" and len(queue) != 0:
                queue.remove(min(queue))

    if len(queue) == 0: return [0, 0]
    return [max(queue), min(queue)]

if __name__ == "__main__":
    print(solution(["I 16","D 1"]))
    print(solution(["I 7","I 5","I -5","D -1"]))
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))