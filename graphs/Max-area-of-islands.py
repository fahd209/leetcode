class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        understanding:
            1. input: matrix with 0's and 1's 
                    0: water
                    1: islands

            2. for loop until i find a 1 then do a dfs to count the cells that are 1
        """

        max_area = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(self.dfs(visited, r, c, grid), max_area)
        
        return max_area

    def dfs(self, visited, r, c, grid):

        if (r, c) in visited:
            return 0

        if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
            return 0

        if grid[r][c] == 0:
            return 0

        visited.add((r, c))

        return (1 + self.dfs(visited, r - 1, c, grid) 
                + self.dfs (visited, r + 1, c, grid) 
                + self.dfs(visited, r, c - 1, grid) 
                + self.dfs(visited, r, c + 1, grid))
