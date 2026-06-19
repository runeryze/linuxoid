class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        current_permutation = []

        visited = set()

        def backtrack():
            if len(current_permutation) == len(nums):
                result.append(current_permutation[:])
                return

            for num in nums:
                if num in visited:
                    continue

                current_permutation.append(num)
                visited.add(num)

                backtrack()

                current_permutation.pop()
                visited.remove(num)

        backtrack()
        return result
