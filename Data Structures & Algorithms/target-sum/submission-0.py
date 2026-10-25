class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            new = {}
            for s in dp:
                new[s + num] = new.get(s + num, 0) + dp[s]
                new[s - num] = new.get(s - num, 0) + dp[s]
            dp = new

        return dp.get(target, 0)