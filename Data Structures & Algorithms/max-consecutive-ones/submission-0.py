class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        sol = 0
        for num in nums:
            if num == 0:
                sol = max(count, sol)
                count = 0
            else:
                count += 1
        
        return max(count, sol)
            