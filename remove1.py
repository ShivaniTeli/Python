from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
               nums[i] = nums[j]
               i += 1
               print("After removing Element", + nums[i])
        return i

print("" + Solution().removeElement([3,2,1,5,6], 3))

