class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = 1
        postfix_mul = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i]=prefix_mul
            prefix_mul*=nums[i]
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix_mul
            postfix_mul *=nums[i]
        return result