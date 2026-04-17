class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastCharIndex = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in lastCharIndex and lastCharIndex[s[right]] >= left:
                left = lastCharIndex[s[right]] + 1

            lastCharIndex[s[right]] = right
            max_len = max(max_len, right - left + 1)
            print(lastCharIndex)
        return max_len

solution = Solution()

print("abcdacb")
print(solution.lengthOfLongestSubstring("abcdacb"))
