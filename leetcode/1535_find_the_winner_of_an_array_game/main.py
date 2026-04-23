import time
from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        counter = 0
        winner = arr[0]
        while True:
            if counter == k or counter >= len(arr):
                return winner
            if arr[0] >= arr[1]:
                winner = arr[0]
                counter += 1
                arr = [arr[0]] + arr[2:] + [arr[1]]
            else:
                winner = arr[1]
                counter = 1
                arr = [arr[1]] + arr[2:] + [arr[0]]
        return winner


s = Solution()
arr = [1,11,22,33,44,55,66,77,88,99]

k = 1000000000
print(s.getWinner(arr, k))
