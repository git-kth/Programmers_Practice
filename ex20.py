# level1 - x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    start = x
    for _ in range(n):
        answer.append(start)
        start += x
    return answer
