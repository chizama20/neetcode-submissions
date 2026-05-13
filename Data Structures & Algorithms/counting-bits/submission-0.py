class Solution:
    def count(self, i):
        count = 0 
        while i > 0:
            if i & 1 == 1:
                count += 1
            i = i >> 1
        return count 

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):    
            res.append(self.count(i))
        return res
        