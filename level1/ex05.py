# level1 - 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = sorted(list(filter(lambda x : x % divisor == 0, arr)))
    return answer or [-1]
