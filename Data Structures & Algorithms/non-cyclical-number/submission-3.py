class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n: int) -> int:
            acc = 0
            while n:
                acc += (n % 10)**2
                n = n // 10
            return acc
        
        fast, slow = n, n
        while fast != 1:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
            if slow == fast:
                return slow == 1

        return True
