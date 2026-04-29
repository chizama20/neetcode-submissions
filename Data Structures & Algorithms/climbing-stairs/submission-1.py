class Solution:
    def climbStairs(self, n: int) -> int:

        def mem(cache, n):

            if n <= 2:
                return n
            if n in cache:
                return cache[n]

            cache[n] = mem(cache, n - 1) + mem(cache, n - 2)
            return cache[n]
        return mem({}, n)