class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if there is only one zero, other are zero expect
        multiple = 1
        zero_index = set()
        zero_count = 0
        result = []
        for index,value in enumerate(nums):
            if value != 0:
                multiple*=value
            else:
                zero_index.add(index)
                zero_count+=1
        if zero_count > 1:
            result = [0]*len(nums)
        elif zero_count == 1:
            for index in range(len(nums)):
                if index in zero_index:
                    result.append(multiple)
                else:
                    result.append(0)
        else:
            for index in range(len(nums)):
                result.append(multiple//nums[index])
        return result