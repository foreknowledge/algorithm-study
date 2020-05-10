from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    current_weight = 0
    push_truck_index = 0
    pop_truck_index = 0
    passing_trucks = deque()

    while True:
        time += 1

        if len(passing_trucks) > 0 and passing_trucks[0] + bridge_length == time:
            passing_trucks.popleft()
            current_weight -= truck_weights[pop_truck_index]
            pop_truck_index += 1            
        
        if push_truck_index < len(truck_weights):
            truck_weight = truck_weights[push_truck_index]
            if current_weight + truck_weight <= weight:
                passing_trucks.append(time)
                current_weight += truck_weight
                push_truck_index += 1

        if len(passing_trucks) == 0:
            return time


if __name__ == "__main__":
    print(solution(5, 10, [7,4,2,8,5,3]))