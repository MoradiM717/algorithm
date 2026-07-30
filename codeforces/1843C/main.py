import math


class Solution:

    def solve(self):
        vertices = self.read()
        return self.solution(vertices=vertices)

    def read(self) -> list[int]:
        n = int(input())
        vertices = [0] * n
        for i in range(n):
            vertices[i] = int(input())
        return vertices

    @staticmethod
    def sum_vertices_in_path(v: int):
        if v == 1:
            return v
        value = v
        layers = int(math.log2(v))
        get_parent = lambda x: int(x / 2 if x % 2 == 0 else (x - 1) / 2)
        for _ in range(layers):
            v = get_parent(v)
            value += v
        return value

    def solution(self, vertices: list[int]):
        results = []
        for v in vertices:
            results.append(self.sum_vertices_in_path(v))
        for res in results:
            print(res)


s = Solution().solve()
