# Base case: if there are no more adjeacent pixcels with the same color
# Base case: if fill (image[sr][sc]) = color then no changes apply
# recursive call checking the neighboring elements to ensure they equal the same value as color

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        starting = image[sr][sc] 
        ROWS, COLS = len(image), len(image[0])
        
        def dfs(sr, sc):
            if min(sr, sc) < 0 or sr >= ROWS or sc >= COLS:
                return image
                
            if image[sr][sc] != starting:
                return image
            image[sr][sc] = color

            dfs(sr + 1, sc)
            dfs(sr - 1, sc)
            dfs(sr, sc + 1)
            dfs(sr, sc - 1)
        dfs(sr, sc)
        return image