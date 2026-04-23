from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        p1, p2, p3 = 0, 1, 2
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return n <= 1
        if len(flowerbed) == 2 and all([place == 0 for place in flowerbed]):
            return n <= 1
        placeable = 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            placeable += 1
            p1 += 1
            p2 += 1
            p3 += 1
        all_empty = lambda x, y, z: x == 0 and y == 0 and z == 0
        last_strike = True
        while p3 < len(flowerbed):
            last_strike = False
            if all_empty(flowerbed[p1], flowerbed[p2], flowerbed[p3]):
                placeable += 1
                p1 += 2
                p2 += 2
                p3 += 2
                last_strike = True
            else:
                p1 += 1
                p2 += 1
                p3 += 1

        if flowerbed[-1] == 0 and flowerbed[-2] == 0 and flowerbed[-3] == 1:
            placeable += 1
        elif last_strike and (p3 -1) < len(flowerbed) and all_empty(flowerbed[p1-1], flowerbed[p2-1], flowerbed[p3-1]):
            placeable += 1

        return n <= placeable


s = Solution()
print(s.canPlaceFlowers([0] , 1))
