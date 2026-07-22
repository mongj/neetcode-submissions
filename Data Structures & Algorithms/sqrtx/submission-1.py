class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = low + (high - low) // 2
            guess = mid**2
            if guess == x:
                return mid
            if guess > x:
                high = mid - 1
            else:
                low = mid + 1
        return high