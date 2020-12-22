def solution(t):
    dp = [t[0], []]
    n = len(t)
    for i in range(1, n):
        for x, y, z in zip([0]+dp[0], dp[0] + [0], t[i]):
            dp[1].append(max(x, y) + z)
        dp.pop(0)
        dp.append([])
    return max(dp[0])