class Solution:

    def solve(self):
        return self.solution(x=self.read())

    def read(self) -> list[int]:
        return int(input())

    def solution(self, x: int):
        print(x * x + (x - 1) * (x - 1))


s = Solution().solve()
