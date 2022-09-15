class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        middle = int(len(nums) / 2)
        
        print(nums)
        print(middle)
        
        if len(nums) == 1 and nums[middle] != target:
            return -1
        
        if nums[middle] == target:
            return middle
        
        if nums[middle] < target:
            r = self.search(nums[middle:], target)
            if r == -1:
                return -1
            return middle + r
        
        if nums[middle] > target:
            return self.search(nums[:middle], target)
        
        
        