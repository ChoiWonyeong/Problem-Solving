from collections import defaultdict
def solution(prices):
    answer = [0 for i in range(len(prices))]
    stack = []
    stack.append(0)
    answer[0]+=1
    for i in range(1, len(prices)-1):
        while len(stack)>0 and prices[stack[-1]]>prices[i]:
            stack.pop(-1)
        stack.append(i)
        # print(stack)

        for j in stack:
            answer[j]+=1
    return answer