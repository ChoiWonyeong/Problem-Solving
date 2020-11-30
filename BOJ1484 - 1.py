# 2020/12/01
# G = (a - b)(a + b)
# a - b > a + b인 경우에만 a값을 구함.
import sys
N = int(input())
i = 1
answer = []
while True:
    a = i
    if N%a!=0:
        i+=1
        continue
    else:
        b = N//a
        if a>=b:
            break
        if((a+b)%2==0):
            answer.append((a+b)//2)
        i+=1
    if a<b:
        continue
    break
for i in sorted(answer):
    print(i)
if len(answer)==0:
    print(-1)