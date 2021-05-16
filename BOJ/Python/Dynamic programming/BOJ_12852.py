# BOJ_12852 1로 만들기 2

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    # [[횟수, [과정]]]
    dp = [[0, []] for _ in range(n+1)]
    
    dp[1][0] = 0
    dp[1][1] = [1]

    for i in range(2, n+1):
        dp[i][0] = dp[i-1][0] + 1
        dp[i][1] = dp[i-1][1] + [i]

        if i % 3 == 0 and dp[i//3][0] + 1 < dp[i][0]:
            dp[i][0] = dp[i//3][0] + 1
            dp[i][1] = dp[i//3][1] + [i]

        if i % 2 == 0 and dp[i//2][0] + 1 < dp[i][0]:
            dp[i][0] = dp[i//2][0] + 1
            dp[i][1] = dp[i//2][1] + [i]

    print(dp[n][0])
    print(' '.join(map(str, dp[n][1][::-1])))

solution()