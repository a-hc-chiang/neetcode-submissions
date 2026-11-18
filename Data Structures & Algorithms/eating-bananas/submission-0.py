class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        total_bananas = sum(piles)
        n = len(piles)
        def can_eat(eating_speed):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / eating_speed)
            return total_hours <= h
        slowest, fastest = 1, max(piles)
        candidate = -1
        while slowest <= fastest:
            mid = (slowest + fastest) // 2
            if can_eat(mid):
                candidate = mid
                fastest = mid - 1
            else:
                slowest = mid + 1
        return candidate