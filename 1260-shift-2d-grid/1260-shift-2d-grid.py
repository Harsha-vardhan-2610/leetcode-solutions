class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not k:
            return grid

        r, c = len(grid), len(grid[0])
        n = r * c
        k %= n

        if not k:
            return grid
        
        def move(i, j):
            while i < j:
                grid[i // c][i % c], grid[j // c][j % c] = grid[j // c][j % c], grid[i // c][i % c]
                i += 1
                j -= 1
                
        move(0, n - 1)
        move(0, k - 1)
        move(k, n - 1)

        return grid