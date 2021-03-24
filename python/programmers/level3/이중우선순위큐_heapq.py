import heapq

def solution(operations):
    minHeap = []

    for o in operations:
        operation, value = o.split()
        if operation == "I": 
            heapq.heappush(minHeap, int(value))
        elif operation == "D":
            if value == "1" and len(minHeap) != 0:
                minHeap.remove(max(minHeap))
            elif value == "-1" and len(minHeap) != 0:
                heapq.heappop(minHeap)

    return [max(minHeap), minHeap[0]] if minHeap else [0, 0]

if __name__ == "__main__":
    print(solution(["I 16","D 1"]))
    print(solution(["I 7","I 5","I -5","D -1"]))
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))