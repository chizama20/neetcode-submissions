class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x*x + y*y  
            heap.append((dist, [x, y]))

        heapq.heapify(heap)

        ans = []
        for _ in range(k):
            dist, point = heapq.heappop(heap)
            ans.append(point)

        return ans