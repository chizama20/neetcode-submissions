class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkDup = []

        for num in nums:
            if num in checkDup:
                return True
            else:
                checkDup.append(num)
        return False