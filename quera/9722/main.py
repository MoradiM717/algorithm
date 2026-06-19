import math


class Solution:        

    def solve(self):
        n = self.read()
        return self.solution(n=n)

    def read(self) -> int:
        return int(input())
    
    @staticmethod
    def _is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    @classmethod
    def _find_successors(cls, candidate: int, length: int):
        if int(math.ceil(math.log10(candidate))) == length:
            print(candidate)
            return
        
        for digit in (1, 3, 7, 9):
            new_candidate = candidate * 10 + digit
            if cls._is_prime(new_candidate):
                cls._find_successors(candidate=new_candidate, length=length)       


    def solution(self, n: int):
        self._find_successors(2, n)
        self._find_successors(3, n)
        self._find_successors(5, n)
        self._find_successors(7, n)


s = Solution().solve()

