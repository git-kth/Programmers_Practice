# level1 - 정수 내림차순으로 정렬하기
def solution(n):
    answer = 0
    number = sorted(list(str(n)))
    for i,v in enumerate(number):
        answer += (10 ** i) * int(v)
    return answer
