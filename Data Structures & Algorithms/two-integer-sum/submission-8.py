class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        
        res = {}
        i = 0
        for num in nums:
            res[num] = i
            i += 1
         
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in res and res[goal] != i:    
                return [i, res[goal]]

                