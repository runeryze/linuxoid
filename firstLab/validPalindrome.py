class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        cleaned_s = ""

        for char in s:
            if char.isalnum():
                cleaned_s += char

        return cleaned_s == cleaned_s[::-1]
