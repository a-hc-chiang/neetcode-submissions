class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left, max_count = 0, 0
        characters = [0] * 26 # all alphabet characters

        for right in range(len(s)):
            characters[ord(s[right]) - 65] += 1
            while sum(characters) - max(characters) > k:
                characters[ord(s[left]) - 65] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res