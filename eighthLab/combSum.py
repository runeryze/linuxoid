class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        current_combination = []

        def backtrack(index, current_sum):
            if current_sum == target:
                result.append(current_combination[:])
                return

            if current_sum > target or index >= len(candidates):
                return

            current_combination.append(candidates[index])
            backtrack(index, current_sum + candidates[index])

            current_combination.pop()
            backtrack(index + 1, current_sum)

        backtrack(0, 0)
        return result
