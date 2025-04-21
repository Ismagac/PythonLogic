from functools import lru_cache

class Solution:
    def racecar(self, target: int) -> int:
        @lru_cache(None)
        def dp(t: int) -> int:
            n = t.bit_length()
            if t == (1 << n) - 1:
                return n

            overshoot = n + 1 + dp((1 << n) - 1 - t)

            undershoot = float('inf')
            for m in range(n-1):
                distance_forward = (1 << (n-1)) - 1
                distance_backward = (1 << m) - 1
                steps = (n-1) + 1 + m + 1 + dp(t - distance_forward + distance_backward)
                undershoot = min(undershoot, steps)

            return min(overshoot, undershoot)

        return dp(target)


if __name__ == "__main__":
    sol = Solution()
    tests = [3, 6, 4, 5, 10]
    for t in tests:
        print(f"target = {t:2d} -> pasos mínimos = {sol.racecar(t)}")
