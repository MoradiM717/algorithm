class Solution:        

    def solve(self):
        self.read()
        return self.solution(self.x, self.prices)

    def read(self):
        line = input()
        _, self.x = map(int, line.split(" "))
        line = input()
        self.prices = [int(price) for price in line.split(" ")]
        

    def solution(self, x: int, prices: list[int]) -> int:
        if len(prices) < 1:
            return 0
        if len(prices) == 1:
            return 1
        
        prices.sort()
        count = 1
        curr = prices[0]
        for i in range(1, len(prices)):
            if curr + prices[i] > x:
                return count
            else:
                count += 1
                curr = max(curr, prices[i])
        return count




s = Solution()
print(s.solve())
