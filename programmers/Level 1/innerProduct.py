# Programmers 01/23 2021
# 내적

def solution(a, b):
    answer = 0

    for i in range(0, len(a)):
        answer += a[i] * b[i]

    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))