class Solution:        

    def solve(self):
        k, a, b = self.read()
        return self.solution(k, a, b)

    def read(self) -> tuple[int, ...]:
        return tuple(map(int, input().split(" ")))
    
    @staticmethod
    def _find_edge_for_k(x: int, k: int) -> int:
        p = x % k
        if p <= k/2:
            return x - p
        else:
            return x - p + k

    def solution(self, k: int, a: int, b: int) -> int:
        if a == b:
            return 0
        
        diff = b - a
        start = self._find_edge_for_k(a, k)
        diff_start = abs(start - a)
        end = self._find_edge_for_k(b, k)
        diff_end = abs(end - b)
        steps_with_k = (end - start) // k
        return min(
            diff,
            steps_with_k + diff_start + diff_end
        )


s = Solution()
print(s.solve())
