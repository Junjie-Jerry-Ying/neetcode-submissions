class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i]-1 not in setnums:
                length = 0
                while nums[i]+ length in setnums:
                    length += 1
                longest = max(length, longest)
        return longest



