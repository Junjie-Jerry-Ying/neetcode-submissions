class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in nums:
            if (num-1) not in num_set:
                curr_len = 0
                while (num+curr_len) in num_set:
                    curr_len+=1
                if curr_len>max_len:
                    max_len = curr_len
        return max_len
            