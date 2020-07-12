# level1 - 다트 게임
def solution(dartResult):
    answer = 0
    dartResult = list(dartResult.replace('10','t'))
    for i in range(len(dartResult)):
        if dartResult[i] == 't':
            dartResult[i] = '10'
    score = [0, 0, 0]
    bonus_type = ['S','D','T']
    idx = -1
    for i in dartResult:
        if i in bonus_type:
            score[idx] = score[idx] * score[idx] ** bonus_type.index(i)
        elif i == '*':
            score[idx] = score[idx] * 2
            if idx != 0:
                score[idx - 1] = score[idx - 1] * 2
        elif i == '#':
            score[idx] = score[idx] * (-1)
        else:
            idx += 1
            score[idx] = int(i)     
    answer = sum(score)
    return answer
