class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break                          # sorted: nothing left can sum to 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue                       # skip duplicate first numbers

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1                 # skip duplicate second numbers
        return res

# [-4, -1, -1, 0, 1, 2] -> -2