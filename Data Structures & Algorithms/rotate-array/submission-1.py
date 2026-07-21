class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, n: List[int], l: int, r: int) -> None:
        while l < r:
            n[l], n[r] = n[r], n[l]
            l, r = l + 1, r - 1
        



        