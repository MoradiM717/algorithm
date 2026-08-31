import sys

INPUT = sys.stdin.readline


class Solution:

    def solve(self):
        test_cases = self.read()
        for tc in test_cases:
            print(self.solution(*tc))

    def read(self) -> list[tuple[list[list[int]], int]]:
        n = int(INPUT().strip())
        test_cases = []
        for _ in range(n):
            t1, _, limit = map(int, INPUT().split(" "))
            values: list[list[int]] = []
            for _ in range(t1):
                line = INPUT()
                values.append([int(v) for v in line.split(" ")])
            test_cases.append((values, limit))
        return test_cases

    @staticmethod
    def _calculate(values: list[int], limit: int) -> tuple[int, int]:
        penalty = 0
        solved = 0
        time_elapsed = 0
        for v in sorted(values):
            if time_elapsed + v > limit:
                break
            solved += 1
            penalty += v + time_elapsed
            time_elapsed += v
        return solved, penalty

    @staticmethod
    def _compare(values: list[int], limit: int, rp: int, rs: int) -> bool:
        penalty = 0
        solved = 0
        time_elapsed = 0
        for v in sorted(values):
            if time_elapsed + v> limit:
                break
            solved += 1
            penalty += v + time_elapsed
            time_elapsed += v
            if solved > rs:
                return True
        return rs < solved or (rs == solved and penalty < rp)

    def solution(self, p: list[list[int]], limit: int):
        rs, rp = self._calculate(p[0], limit)
        rank = 1
        for i in range(1, len(p)):
            if self._compare(p[i], limit, rp, rs):
                rank += 1
        return rank
    
Solution().solve()
