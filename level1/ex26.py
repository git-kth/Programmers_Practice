# level1 - 소수 찾기
from math import sqrt
def solution(n):
    answer = 1
    for i in range(3,n + 1,2):
        answer += 1
        for j in range(2,int(sqrt(i)) + 1):
            if i % j == 0:
                answer -= 1
                break
    return answer
