from collections import defaultdict
class Solution:

    def solve(self):
        teams = self.read()
        return self.solution(teams)

    def read(self) -> list[int]:
        input()
        line = input()
        return list(map(int, line.split(" ")))
    
    @staticmethod
    def _calculate_minimum_k(indexes: list[int]) -> int:
        gaps = []
        for i in range(1, len(indexes)):
            gaps.append(indexes[i] - indexes[i - 1])
        return max(gaps)

    def solution(self, teams: list[int]) -> int:
        mapper: dict[int, list[int]] = defaultdict(list)
        for idx in range(len(teams)):
            mapper[teams[idx]].append(idx)

        for key in mapper.keys():
            mapper[key] = [-1] + mapper[key] + [len(teams)]

        return min(
            [self._calculate_minimum_k(team) for team in mapper.values()]
        )


s = Solution()
print(s.solve())
