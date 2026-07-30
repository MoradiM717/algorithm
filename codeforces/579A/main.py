from collections import defaultdict
class Solution:        

    def solve(self):
        return self.solution(self.read())

    def read(self) -> int:
        return int(input())

    def solution(self, n: int):
        count = 0
        for char in bin(n).split("b")[1]:
            if char == "1":
                count += 1
        return count

s = Solution().solve()
print(s)
