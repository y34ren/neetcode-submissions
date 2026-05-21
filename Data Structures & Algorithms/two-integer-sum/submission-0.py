from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for i in range (len(nums)):
            targ = target - nums[i]
            if targ in seen:
                return [seen[targ],i]
            else:
                seen[nums[i]] = i
        