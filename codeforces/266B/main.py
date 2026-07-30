from typing import Optional


class Solution:        

    def solve(self):
        t, line = self.read()
        for _ in range(t):
            line = self.solution(line=line)
        return line

    def read(self) -> tuple[int, list[str]]:
        t = int(input().split(" ")[1])
        line = input()
        return t, [char for char in line]

    @staticmethod
    def _find_boy_pointer(line: list[str]) -> Optional[int]:
        for i in range(len(line) - 1):
            if line[i] == "B" and line[i + 1] == "G":
                return i
            
    @staticmethod
    def _find_girl_pointer(line: list[str]) -> Optional[int]:
        has_met_a_boy = False
        for i in range(len(line)):
            if has_met_a_boy and line[i] == "G":
                return i

            if line[i] == "B":
                has_met_a_boy = True

    def solution(self, line: list[str]) -> list[str]:
        boy_pointer = self._find_boy_pointer(line)
        girl_pointer = self._find_girl_pointer(line)
        if boy_pointer is None and girl_pointer is None:
            return line
        line[boy_pointer], line[girl_pointer] = line[girl_pointer], line[boy_pointer]
        return line[:girl_pointer + 1] + (self.solution(line[girl_pointer + 1:]) if girl_pointer + 1 < len(line) else [])

        
            

s = Solution().solve()
print("".join(s))
