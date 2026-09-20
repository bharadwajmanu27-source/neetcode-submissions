class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0,11):

            if i not in nums:
                return i