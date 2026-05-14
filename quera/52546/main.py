class Solution:        

    def solve(self):
        self.read()
        return self.solution(self.s, self.arr)

    def read(self):
        self.s = input()
        n = int(input())
        self.arr = []
        for _ in range(n):
            self.arr.append(input())

    def solution(self, s: str, ts: list[str]) -> int:
        end_idx = len(s)
        count = 0
        for ts_str in ts:
            idx = 0
            for char in ts_str:
                if idx == end_idx:
                    break
                if char == s[idx]:
                    idx += 1
            if idx == end_idx:
                count += 1
        return count


s = Solution()
print(s.solve())
