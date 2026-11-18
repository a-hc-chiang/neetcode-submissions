class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        candidate = -1 
        last_element = nums[-1]

        # condition: is rotated? then mid > end move towards right 
        # not rotated? then mid < end move towards left 
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > last_element: # move right 
                left = mid + 1
            elif nums[mid] < last_element: # move left 
                candidate = mid
                right = mid - 1
            else:
                candidate = mid
                left = mid + 1
        return nums[candidate]
