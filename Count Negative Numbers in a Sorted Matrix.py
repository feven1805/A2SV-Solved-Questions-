class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] < 0:
                    count += 1
                else:
                    count += 0
        return count
