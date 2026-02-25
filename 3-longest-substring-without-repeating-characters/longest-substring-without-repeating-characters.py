class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        longest = 0
        seen = set()
        length = 0

        while right < n:
            if s[right] not in seen:
                seen.add(s[right])
                length = right - left + 1
                longest = max(longest, length)
                right += 1
                
            else:
                seen.remove(s[left])
                left += 1
        return longest

