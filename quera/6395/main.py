class Solution:        

    def solve(self):
        costs = self.read()
        return self.solution(costs=costs)

    def read(self):
        input()
        return list(map(int, input().split(" ")))


    def solution(self, costs: list[int]):
        differences = 0
        curr = 0
        for cost in costs:
            diff = curr - cost
            if diff < 0:
                differences += abs(diff)
                curr = 0
            else:
                curr -= cost
        return differences


s = Solution().solve()
print(s)