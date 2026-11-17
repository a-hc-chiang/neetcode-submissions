class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right: 
            mid = (left + right) // 2
            curr = mid * mid 
            if curr == x: 
                return mid 
            elif curr < x: 
                left = mid + 1
            else:
                right = mid - 1
        return left - 1