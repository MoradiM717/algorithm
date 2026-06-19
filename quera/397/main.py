class Solution:        

    def solve(self):
        chars = self.read()
        return self.solution(chars=chars)

    def read(self):
        return input()
        
    def solution(self, chars: str) -> int:
        stack = []
        for char in chars:
            if char == "(":
                stack.append(char)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(char)
        if not stack:
            return 0
        o = 0
        c = 0
        for item in stack:
            if item == "(":
                o += 1
            else:
                c += 1
        return (c + 1) // 2 + (o + 1) // 2

s = Solution()
print(s.solve())


