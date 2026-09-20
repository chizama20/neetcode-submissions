class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for num in nums:
            res[num] += 1        
        
        sol = sorted(res, key=res.get, reverse=True)
        
        n = []
        i = 0
        while i < k:
            n.append(sol[i])
            i += 1
        return n