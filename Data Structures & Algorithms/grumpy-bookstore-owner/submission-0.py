class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        baseSatisfiedCount = sum([c for i, c in enumerate(customers) if grumpy[i] == 0])
        maxAdditionalSatisfiedCustomers = 0
        for i in range(len(customers) - minutes + 1):
            additionalSatisfiedCustomers = 0
            for j in range(i, i + minutes):
                if grumpy[j] == 1:
                    additionalSatisfiedCustomers += customers[j]
            maxAdditionalSatisfiedCustomers = max(maxAdditionalSatisfiedCustomers, additionalSatisfiedCustomers)
        return baseSatisfiedCount + maxAdditionalSatisfiedCustomers