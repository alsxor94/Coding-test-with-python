# 옳바른 문자열 u와  그렇지 않은 문자열 v를 어떻게 나눌 것인가.
# 카운트는 여러 개 만들면 안됌.
# 하나로 하고, 대신 uv를 어떻게 구별할 것인지 생각해야됌.
def solution(p):
    cnt = 0
    u = ''
    v = ''
    answer = ''
    while p:
        a = p.pop(0)
        if cnt == 0 and a == '(':
            u += a
            cnt += 1
            while cnt > 0:
                a = p.pop(0)
                if cnt > 0 and a == ')':
                    u += a
                    cnt -= 1
                elif cnt > 0 and a == '(':
                    u += a
                    cnt += 1
            answer += u
            u = ''
        elif cnt ==0 and a == ')':
            v += a
            cnt -= 1
            while cnt < 0:
                a = p.pop(0)
                if cnt < 0 and a == ')':
                    v += a
                    cnt -= 1
                elif cnt < 0 and a == '(':
                    v += a
                    cnt += 1
            for i in v:
                if i == ')':
                    answer += '('
                else:
                    answer += ')'
            v =''

    return answer

p = list(input())
solution(p)
