# level1 - 정수 제곱근 판별
from math import sqrt

def solution(n):
    return checkInt(sqrt(n))

def checkInt(x):
    return (x + 1) ** 2 if x == int(x) else -1
