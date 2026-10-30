class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtrack(curr, seen): 
            if len(curr) == len(nums): 
                res.append(curr.copy())
                return 
            for num in nums: 
                if num not in seen: 
                    curr.append(num)
                    seen.add(num)
                    backtrack(curr, seen)
                    seen.remove(num)
                    curr.pop()
        backtrack([], set())
        return res