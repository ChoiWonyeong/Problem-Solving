# 2020/12/01
# G = s^2 - e^2 == N인 모든 경우를 체크
import sys
N = int(input())
s = 1
e = 1
answer = []
G = s*s - e*e
flag = 0
while s<N or e<N:
    if G<N:
        s+=1
    elif G>N:
        e+=1
    else:
        e+=1
        answer.append(s)
    G = s*s - e*e
    flag += 1
for i in sorted(answer):
    print(i)
if len(answer)==0:
    print(-1)