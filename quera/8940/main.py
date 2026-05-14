class Solution:        

    def solve(self):
        self.read()
        return self.solution(self.p, self.q, self.words)

    def read(self):
        line = input()
        n, self.p, self.q = map(int, line.split(" "))
        self.words = []
        for _ in range(n):
            self.words.append(input())

    def solution(self, p: int, q: int, words: list[str]) -> int:
        seen = set()
        for word in words:
            check = (word[:p], word[-q:])
            if check in seen:
                continue
            else:
                seen.add(check)
        return len(seen)


s = Solution()
print(s.solve())
