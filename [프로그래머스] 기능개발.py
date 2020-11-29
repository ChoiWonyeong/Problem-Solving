import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    dq = deque([])
    count = 0
    # 입력받은 인자로 남은 각 작업 별로 남은 작업 일수를 리스트에 저장
    arr = [(100 - i) for i in progresses]
    for i in range(len(arr)):
        arr[i] = math.ceil(arr[i]/speeds[i])
    
    dq.append(arr[0])
    for i in range(1, len(arr)):
        # 현재 남은 작업 일수와 deque의 첫번째 값과 비교해서 더 작으면 추가
        if arr[i]<=dq[0]:
            dq.append(arr[i])
        else:
            # 크면 더 큰 값을 만날 때까지 deque의 값을 계속 제거하면서 count++
            while len(dq)>0 and dq[-1]<arr[i]:
                dq.pop()
                count+=1
            dq.append(arr[i])
            answer.append(count)
            count = 0
    # 마지막에 deque에 남아있는 값들을 추가
    answer.append(len(dq))
    return answer