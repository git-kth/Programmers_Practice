# level1 - 시저 암호
def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ': answer += ' '
        elif c.islower(): answer += chr((ord(c) - 0x61 + n) % 26 + 0x61)
        else: answer += chr((ord(c) - 0x41 + n) % 26 + 0x41)
    return answer
