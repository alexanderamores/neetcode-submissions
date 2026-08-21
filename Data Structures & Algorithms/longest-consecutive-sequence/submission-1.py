class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We make a set based on all the numbers in nums
        numSet = set(nums)
        longest = 0

        # Then we iterate through nums
        for n in numSet:
        # If that number is a start of sequence then count consecutives
        # Means if there is no current number-1 in the set
            if (n - 1) not in numSet:
                count = 0
                while (n + count) in numSet:
                    count += 1
                longest = max(longest, count)
        
        return longest


        