class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = defaultdict(int)
        for i in range(len(nums)):
            goal = target - nums[i] 
            if res[goal]:
                return [res[goal], i + 1]
            res[nums[i]] = i + 1
        return []
        