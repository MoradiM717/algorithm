class Solution:        

    def solve(self):
        infix = self.read()
        return self.solution(infix=infix)

    def read(self) -> str:
        return input()


    def solution(self, infix: str) -> str:
        postfix: str = ""
        stack: list[str] = []
        precedence: dict[str, int] = {
            "+": 1, "-": 1, "*": 2, "/": 2
        }
        idx = 0
        while idx < len(infix):
            char = infix[idx]  
            if char in precedence:
                while stack and precedence[stack[-1]] >= precedence[char]:
                    postfix += stack.pop()
                stack.append(char)
            
            elif char == "(":
                count = 1
                idx += 1
                start = idx
                while count != 0:
                    if infix[idx] == "(":
                        count += 1
                    elif infix[idx] == ")":
                        count -= 1
                    idx += 1
                idx -= 1
                postfix += self.solution(infix[start: idx])

            else:
                postfix += char
            idx += 1
        
        while stack:
            postfix += stack.pop()
        
        return postfix
                

s = Solution().solve()
print(s)
