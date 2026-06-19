class Solution:        

    def solve(self):
        k, queries = self.read()
        return self.solution(k=k, queries=queries)

    def read(self):
        _, k, q = map(int, input().split(" "))        
        queries = []
        for _ in range(q):
            s, d = map(int, input().split(" "))
            if s > d:
                s, d = d, s
            queries.append((s,d))
        return k, queries
    
    @staticmethod
    def _get_parent_value(child_value: int, k: int) -> int:
        return (child_value - 2) // k + 1
    
    @classmethod
    def _find_result(cls, query: tuple[int, int], k: int) -> int:
        s, d = query
        if k == 1:
            return abs(s - d)
        steps = 0
        while s != d:
            if s > d:
                s = cls._get_parent_value(s, k) 
            else:
                d = cls._get_parent_value(d, k)
            steps += 1
        return steps
            

    def solution(self, k: int, queries: list[tuple[int, int]]):
        for query in queries:
            print(self._find_result(query=query, k=k))
        

s = Solution()
s.solve()
