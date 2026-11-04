class Solution:
    def reverseBits(self, n: int) -> int:
        res, curr = 0, 31
        while n > 0:
            if n & 1:
                res += 2 ** curr
            n >>= 1
            curr -= 1  
        return res