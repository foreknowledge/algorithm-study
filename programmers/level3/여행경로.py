# -*- coding: utf-8 -*-

def solution(tickets):
    ticket_map = dict()

    for t in tickets:
        ticket_map[t[0]] = ticket_map.get(t[0], []) + [t[1]]
    for k in ticket_map:
        ticket_map[k].sort(reverse=True)

    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        # top에서 출발하는 ticket이 없는 경우
        if top not in ticket_map or len(ticket_map[top]) == 0:
            # top을 path에 추가
            path.append(stack.pop())
        else:
            # 알파벳 순서의 첫 번째 도착지 stack에 추가
            stack.append(ticket_map[top][-1])
            # 경유지에서 빼기
            ticket_map[top].pop()

    return path[::-1]

if __name__ == "__main__":
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))