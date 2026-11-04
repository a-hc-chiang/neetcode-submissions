class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        def best_next(start, end):
            # index in [start, end] whose reach (i + nums[i]) is farthest
            best_idx, best_reach = start, start + nums[start]
            for i in range(start, end + 1):
                if i + nums[i] > best_reach:
                    best_reach = i + nums[i]
                    best_idx = i
            return best_idx

        def jump_recursive(curr_idx, jumps):
            # can we reach the end from here with one more jump?
            if curr_idx + nums[curr_idx] >= n - 1:
                return jumps + 1
            nxt = best_next(curr_idx + 1, curr_idx + nums[curr_idx])
            return jump_recursive(nxt, jumps + 1)

        return jump_recursive(0, 0)