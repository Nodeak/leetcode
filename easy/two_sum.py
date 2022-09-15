class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}  # number : location
        
        for i in range(len(nums)):
            
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            
            d[nums[i]] = i