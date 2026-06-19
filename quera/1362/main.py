BLOCKED = "T"

class Solution:        

    def solve(self):
        road = self.read()
        return self.solution(road=road)

    def read(self):
        input() # ignoring the n
        line = input()
        return [char for char in line]
        

    def solution(self, road: list[str]) -> int:
        dp: list[int] = [0 for _ in range(len(road))]
        starting_point = 0
        for i in range(3):
            if road[starting_point] == BLOCKED:
                starting_point = i
            else:
                break
        if road[starting_point] == BLOCKED:
            return 0
        dp[starting_point] = 1
        for i in range(starting_point + 1, len(dp)):
            if road[i] == BLOCKED:
                dp[i] = 0
                continue
            value = 0
            if i - 1 >= 0:
                value += dp[i - 1]
            if i - 2 >= 0:
                value += dp[i - 2]
            if i - 3 >= 0:
                value += dp[i - 3]
            dp[i] = value
        return dp[-1]

s = Solution()
print(s.solve())


