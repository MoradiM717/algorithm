from collections import defaultdict
class Solution:        

    def solve(self):
        return self.solution(*(self.read()))

    def read(self) -> tuple[int, int]:
        return map(int, input().split(" "))

    @staticmethod
    def lowbit(n: int):
        return 2 ** ( (n & -n).bit_length() - 1 )


    def solution(self, s: int, l: int):
        box: dict[int, list[int]] = defaultdict(list)

        for i in range(1, l + 1):
            v = self.lowbit(i)
            if v in box:
                return box[v] + [v]
            box[s - v].append(i)


s = Solution().solve()
print(s)
