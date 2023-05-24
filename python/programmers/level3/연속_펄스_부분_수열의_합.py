def solution(sequence):
    s0 = sequence[0]
    m1, m2 = s0, -s0
    p_m1, p_m2 = s0, -s0

    for i in range(1, len(sequence)):
        s = sequence[i] * (-1 if i % 2 else 1)
        p_m1 = max(p_m1+s, s)
        m1 = max(m1, p_m1)
        p_m2 = max(p_m2-s, -s)
        m2 = max(m2, p_m2)

    return max(m1, m2)


print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
