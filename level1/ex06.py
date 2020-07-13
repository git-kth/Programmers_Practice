# level1 - 체육복
def solution(n, lost, reserve):
    std = [1 for i in range(n)]
    for i in reserve: std[i - 1] = 2
    for i in lost: std[i - 1] = std[i - 1] - 1
    for i in range(n):
        if not std[i]:
            if i > 0 and std[i - 1] == 2: std[i] = std[i - 1] = 1
            elif i < n - 1 and std[i + 1] == 2: std[i] = std[i + 1] = 1  
    answer = len(list((filter(lambda x : x > 0,std))))
    return answer
