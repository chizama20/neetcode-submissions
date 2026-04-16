class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for lis in matrix:
            ba = lis[-1]
            if target > ba:
                continue
            else:
                for num in lis:
                    if target == num:
                        return True
        
        return False