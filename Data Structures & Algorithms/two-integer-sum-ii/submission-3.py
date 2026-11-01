class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, value in enumerate(numbers):
            other_i = len(numbers) - 1
            other = numbers[other_i]
            while (value + other > target):
                other_i -= 1
                other = numbers[other_i]
            if (value + other == target):
                return [index+1, other_i+1]



