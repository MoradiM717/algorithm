import sys

INPUT = sys.stdin.readline


class Solution:

    def solve(self):
        n = int(INPUT().strip())
        answers = []
        for _ in range(n):
            t = int(INPUT())
            line = INPUT()
            p = [int(v) for v in line.split()]
            answers.append(self.solution(t, p))
        for i in range(n):
            print(answers[i])

    @staticmethod
    def _iterate(p: list[int], target: int) -> tuple[int, list[int]]:
        counter = 1
        curr = p[target - 1]
        seen = [curr]
        while curr != target:
            counter += 1
            curr = p[curr - 1]
            seen.append(curr)
        return counter, seen

    def solution(self, n: int, p: list[int]) -> str:
        answers = [-1] * n
        for i in range(n):
            if answers[i] == -1:
                length, whole_path = self._iterate(p, i + 1)
                for node in whole_path:
                    answers[node - 1] = length
        return " ".join([str(v) for v in answers])


Solution().solve()
