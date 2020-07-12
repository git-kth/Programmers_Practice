# level1 - 같은 숫자는 싫어
def solution(arr):
    answer = []
    cmp = -1
    for i in arr:
        if cmp != i:
            answer.append(i)
            cmp = i
    return answer
