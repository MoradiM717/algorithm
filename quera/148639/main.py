class Solution:
    LATEX_PHRASE: str = "\\frac{{{i}}}{{{j}}}"
    def solve(self):
        n = self.read()
        return self.solution(n=n)
    
    def read(self) -> int:
        return int(input())

    def build(self, curr: int, limit: int, level: int):
        if level == limit:
            return ""
        level += 1
        first_phrase = self.build(curr=curr*2, limit=limit, level=level)
        second_phrase = self.build(curr=curr*2 + 1, limit=limit, level=level)
        
        a, b = 2 * curr, 2 * curr + 1
        if first_phrase:
            a = f"{a}+{first_phrase}"
            b = f"{b}+{second_phrase}"
        return self.LATEX_PHRASE.format(i=a, j=b)

    def solution(self, n: int):
        if n == 1:
            return 1
        after_1 = self.build(curr=1, limit=n, level=1)
        return f"1+{after_1}"


print(Solution().solve())