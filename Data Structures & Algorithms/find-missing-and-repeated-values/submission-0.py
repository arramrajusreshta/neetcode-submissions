class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = [x for row in grid for x in row]

        for i in range(1, n * n + 1):
            if nums.count(i) == 2:
                repeated = i
            elif nums.count(i) == 0:
                missing = i

        return [repeated, missing]