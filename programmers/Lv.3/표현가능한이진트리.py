# 표현 가능한 이진 트리
# https://school.programmers.co.kr/learn/courses/30/lessons/150367
def dfs(b, i, depth):
    if depth == 0:
        return True
    
    elif b[i] == '0':   
        if b[i - depth] == '1' or b[i + depth] == '1': return False

    left = dfs(b, i - depth, depth // 2)
    right = dfs(b, i + depth, depth // 2)
    return left and right
    
    
def solution(numbers):
    answer = []
    for num in numbers:
        b = bin(num)[2:]
        nodes = bin(len(b) + 1)[2:]
        
        if '1' in nodes[1:]:       
            dummies = pow(2, len(nodes)) - (len(b)+1)
            b = '0' * dummies + b
            
        result = dfs(b, len(b)//2, (len(b)+1)//4)
        answer.append(1 if result else 0)
        
    return answer

print(solution([7, 42, 5]))