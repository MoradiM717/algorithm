from typing import List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        pointer1 = 0
        pointer2 = 1
        win_count = 0
        while pointer2 < len(arr) and pointer1 < len(arr):
            if win_count == k:
                break
            if arr[pointer1] >= arr[pointer2]:
                win_count += 1
                pointer2 += 1
            else:
                win_count = 1
                pointer1 = pointer2
                pointer2 += 1
        return arr[pointer1]


# from test_case import test_case as arr
arr = [2,1,3,5,4,6,7]

k = 2


s = Solution()
print(s.getWinner(arr=arr, k=k))