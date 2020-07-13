# level1 - 행렬의 덧셈
def solution(arr1, arr2):
    answer = []
    n = len(arr1)
    m = len(arr1[0])
    for i in range(n):
        answer.append([])
        for j in range(m):
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer
