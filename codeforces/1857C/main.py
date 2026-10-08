import sys

INPUT = sys.stdin.readline


def read():
    n = int(INPUT())
    all_cases = [0] * n
    for i in range(n):
        t = int(INPUT())
        line = INPUT()
        nums = [int(v) for v in line.split()]
        all_cases[i] = (t, nums)

    return all_cases


def solution(n: int, nums: list[int]):
    nums.sort()
    pos = 0
    result = []
    counter = n - 1
    while counter > 0:
        result.append(nums[pos])
        pos += counter
        counter -= 1
    if len(result) != n:
        max_value = max(nums)
        result.extend([max_value] * (n - len(result)))
    return result


test_cases = read()
for n, test_case in test_cases:
    print(" ".join(str(v) for v in solution(n, test_case)))
