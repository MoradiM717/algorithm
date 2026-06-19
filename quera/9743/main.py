class Solution:        

    def solve(self) -> list[list[int]]:
        table = self.read()
        return self.solution(table=table)

    def read(self):
        table = []
        for _ in range(9):
            table.append(
                list(
                    map(int, input().split(" "))
                )
            )
        return table

    @staticmethod
    def is_valid(table: list[list[int]])

    def solution(self, table: list[list[int]], row: int = 0, col: int = 0):
        


s = Solution().solve()
print(s)
