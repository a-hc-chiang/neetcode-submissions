class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False 
        target = target // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for curr_sum in range(target, num - 1, -1):
                dp[curr_sum] = dp[curr_sum] or dp[curr_sum-num]
        return dp[target]