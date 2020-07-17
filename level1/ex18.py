# level1 - 자연수 뒤집어 배열로 만들기
def solution(n):
    rev_n = reversed((str(n)))
    return list(map(lambda x : int(x),rev_n))
