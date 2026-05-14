class Solution:
    TOTAL_INVERTIONS: int = 0

    def solve(self):
        heights = self.read()
        return self.solution(heights)

    def read(self) -> list[int]:
        input()
        line = input()
        return list(map(int, line.split(" ")))
    
    @classmethod
    def merge(cls, l1: list[int], l2: list[int]) -> list[int]:
        merged = [0] * (len(l1) + len(l2))
        i1 = 0
        i2 = 0
        idx = 0
        while i1 < len(l1) and i2 < len(l2):
            if l1[i1] < l2[i2]:
                merged[idx] = l1[i1]
                i1 += 1
            else:
                merged[idx] = l2[i2]
                i2 += 1
                cls.TOTAL_INVERTIONS += len(l1) - i1

            idx += 1
        while i1 < len(l1):
            merged[idx] = l1[i1]
            i1 += 1
            idx += 1
        
        while i2 < len(l2):
            merged[idx] = l2[i2]
            i2 += 1
            idx += 1
            cls.TOTAL_INVERTIONS += len(l1) - i1
        
        return merged
    
    @classmethod
    def sort(cls, numbers: list[int]) -> list[int]:
        if len(numbers) < 2:
            return numbers
        mid = len(numbers) // 2
        return cls.merge(
            cls.sort(numbers[:mid]),
            cls.sort(numbers[mid:])
        )

    def solution(self, heights: list[int]) -> int:
        self.sort(heights)
        return self.TOTAL_INVERTIONS


s = Solution()
print(s.solve())
