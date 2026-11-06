import sys
from collections import Counter

INPUT = sys.stdin.readline


def read():
    n = int(INPUT())
    words = ["" for _ in range(n)]
    for i in range(n):
        INPUT()
        words[i] = INPUT().strip()
    return words


def solution(word: str) -> int:
    m = max(Counter(word).values())
    n = len(word)
    return max(2 * m - n, n % 2)


test_cases = read()
for tc in test_cases:
    print(min(solution(tc), solution(tc[::-1])))
