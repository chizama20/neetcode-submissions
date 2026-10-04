class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        high = 0
        for num in nums:
            if num - 1 not in check:
                count = 1
                while num + count in check:
                    count += 1
                high = max(count, high)
                
        return high