import sys
from collections import defaultdict

INPUT = sys.stdin.readline


def read():
    n = int(INPUT())
    all_cases = [0] * n
    for i in range(n):
        t = int(INPUT())
        groups = defaultdict(list)
        for _ in range(t):
            a, b = tuple(map(int, INPUT().split()))
            groups[a].append(b)
        all_cases[i] = (t, groups)
    return all_cases


def solution(n: int, pgroups: dict[int, list[int]]):
    count = 0
    for x in sorted(pgroups.keys()):
        if len(pgroups[x]) == 2:
            count += n - 2
        if (x - 1) in pgroups and (x + 1) in pgroups:
            if 1 in pgroups[x] and 0 in pgroups[x - 1] and 0 in pgroups[x + 1]:
                count += 1
            if 0 in pgroups[x] and 1 in pgroups[x - 1] and 1 in pgroups[x + 1]:
                count += 1
    print(count)


test_cases = read()
for n, test_case in test_cases:
    solution(n, test_case)
