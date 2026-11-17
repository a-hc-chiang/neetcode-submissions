class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right: 
            mid = (left + right) // 2 
            if nums[mid] == target: 
                return mid
            elif nums[mid] > target: # we're too big
                right = mid - 1
            else: # we're too small
                left = mid + 1 

        return -1