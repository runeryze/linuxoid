import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        result = right

        while left <= right:
            mid_speed = left + (right - left) // 2

            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile / mid_speed)

            if hours_spent <= h:
                result = mid_speed
                right = mid_speed - 1
            else:
                left = mid_speed + 1

        return result
