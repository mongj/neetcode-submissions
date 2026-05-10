class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        movedElementCount = 0
        cycleStart = 0
        while movedElementCount < n:
            # start from index 0
            currIndex = cycleStart
            prev = nums[currIndex - k]
            while True:
                # at every step, store current value into next
                # load prev value
                temp = nums[currIndex]
                nums[currIndex] = prev
                prev = temp
                movedElementCount += 1

                currIndex = (currIndex + k ) % n

                if currIndex == cycleStart:
                    break
            cycleStart += 1


        