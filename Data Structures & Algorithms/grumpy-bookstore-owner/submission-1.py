class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        base = 0
        for c, g in zip(customers, grumpy):
            if g == 0:
                base+=c

        extra = 0
        for i in range(minutes):
            extra += customers[i] * grumpy[i]
        max_extra = extra

        for i in range(minutes, len(customers)):
            extra += customers[i] * grumpy[i]
            extra -= customers[i-minutes] * grumpy[i-minutes]
            max_extra = max(extra, max_extra)
        
        return base + max_extra
        