class Solution:        

    def solve(self):
        m, s, rate = self.read()
        return self.solution(m=m, s=s, rate=rate)

    def read(self):
        m = tuple(map(int, input().split(" ")))
        s = tuple(map(int, input().split(" ")))
        rate = int(input())
        return m, s, rate

    def solution(self, m: tuple[int, int], s: tuple[int, int], rate: int):
        budget = m[1] * rate + m[0]
        cost = s[1] * rate + s[0]
        if budget >= cost:
            print("Yes")
        else:
            print("No")


s = Solution().solve()
