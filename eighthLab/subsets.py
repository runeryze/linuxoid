class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        current_subset = []

        def backtrack(index):
            if index == len(nums):
                result.append(current_subset[:])
                return

            current_subset.append(nums[index])
            backtrack(index + 1)

            current_subset.pop()
            backtrack(index + 1)

        backtrack(0)
        return result
