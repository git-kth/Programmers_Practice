# level1 - 약수의 합
def solution(n):
    answer = n
    for i in range(1,n // 2 + 1):
        if n % i == 0: answer += i
    return answer
