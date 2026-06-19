from collections import deque, defaultdict
class Solution:        

    def solve(self):
        n, edges = self.read()
        return self.solution(n=n, edges=edges)

    def read(self) -> tuple[int, list[tuple[int, int]]]:
        n, m = map(int, input().split(" "))
        edges = []
        
        for _ in range(m):
            u, v = map(int, input().split(" "))
            edges.append((u, v))
        return n, edges


    def solution(self, n: int, edges: list[tuple[int, int]]):
        children: dict[int, list[int]] = defaultdict(list)
        weights: list[int] = [0] * (n + 1)
        for at , to in edges:
            children[at].append(to)
            weights[to] += 1

        # Kahn's Algorithm
        queue: deque[int] = deque(i for i in range(1, n + 1) if weights[i] == 0)
        topo_sorting: list[int] = [0] * (n + 1)
        order = 0
        while queue:
            poped = queue.popleft()            
            for child in children[poped]:
                if child in weights:
                    weights[child] -= 1
                if weights[child] == 0:
                    queue.append(child)
            topo_sorting[poped] = order

        for idx, (u, v) in enumerate(edges):
            if abs(topo_sorting[u] - topo_sorting[v]) == 1:
                print(1)
                print(idx + 1)
        
        orig_indegree = [0] * (n + 1)
        for u, v in edges:
            orig_indegree[v] += 1
        for ei, (u, v) in enumerate(edges):
            if orig_indegree[v] == 1:
                print(1)
                print(ei + 1)
                return

s = Solution().solve()
