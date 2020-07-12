# level1 - 2016년
def solution(a, b):
    a = a - 1
    b = b - 1
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    s = sum(month[:a]) + b
    answer = day[s % 7]
    return answer
