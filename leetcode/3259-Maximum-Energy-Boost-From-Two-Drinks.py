class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        def maxEnergyBoost(A, B):
            a1 = b1 = a2 = b2 = 0      # F(0,i-1), F(1,i-1), F(0,i-2), F(1,i-2)
            for x, y in zip(A, B):
                a, b = x + max(a1, b2), y + max(b1, a2)
                a2, b2, a1, b1 = a1, b1, a, b
            return max(a1, b1)

        return maxEnergyBoost(energyDrinkA, energyDrinkB)