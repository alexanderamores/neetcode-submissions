class Solution:
    def findMin(self, nums: List[int]) -> int:
        # We do binary search but instead of looking for a specific target
        # We will fin the min number

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]