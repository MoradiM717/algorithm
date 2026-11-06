import sys

INPUT = sys.stdin.readline

MOD = 10**9 + 7


def read():
    return tuple(map(int, INPUT().split()))


def solution(n: int, m: int):
    dp = [[1 for _ in range(n)] for _ in range(2 * m)]
    for i in range(1, 2 * m):
        for j in range(1, n):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    print(sum(dp[-1]) % MOD)


solution(*read())
