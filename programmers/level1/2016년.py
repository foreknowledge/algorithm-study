def solution(a, b):
    dayOfWeek = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED',]
    daysOfMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    days = b
    for i in range(a-1, 0, -1):
        days += daysOfMonth[i - 1]

    return dayOfWeek[days % 7]

if __name__ == "__main__":
    print(solution(5, 24))