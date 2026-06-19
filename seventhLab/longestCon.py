from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        sub = []

        for num in nums:
            idx = bisect_left(sub, num)

            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num

        return len(sub)
