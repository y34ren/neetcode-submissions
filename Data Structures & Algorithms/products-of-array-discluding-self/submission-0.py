from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range (len(nums)):
            if i == 0:
                result.append(prod(nums[1:]))
            elif i == len(nums) -1:
                result.append(prod(nums[:-1]))
            else:
                ls = nums[:i] + nums[i+1:]
                result.append(prod(ls))
        return result 

        