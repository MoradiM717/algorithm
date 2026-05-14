class Solution:        

    def solve(self):
        n = self.read()
        return self.solution(n)

    def read(self):
        return int(input())
    
    @staticmethod
    def _count(n: int, target: int):
        counter = 0
        while n % target == 0:
            n = n // target
            counter += 1
        return counter

    @classmethod
    def _calculate_factorial(cls, n: int) -> int:
        result = 1
        twos = 0
        fives = 0
        for i in range(n, 1, -1):
            x = i

            while x % 2 == 0:
                twos += 1
                x //= 2
            
            while x % 5 == 0:
                fives += 1
                x //= 5
            
            result = (result * x) % 10
        for _ in range(twos - fives):
            result = (result * 2) % 10
        return result
        
    def solution(self, n: int):
        factorial = self._calculate_factorial(n)
        return factorial


s = Solution()
print(s.solve())
