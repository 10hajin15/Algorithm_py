# 점프와 순간이동
# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    answer = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            answer += 1
    return answer

print(solution(5))
print(solution(6))
print(solution(5000))