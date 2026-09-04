class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = [[] for _ in range(length)]
        self.currSnapshotId = 0

    def set(self, index: int, val: int) -> None:
        self.snapshots[index].append((self.currSnapshotId, val))

    def snap(self) -> int:
        self.currSnapshotId += 1
        return self.currSnapshotId - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id >= self.currSnapshotId:
            return 0

        # binary search the snapshots for the given index
        # to find the last updated value
        snapshot = self.snapshots[index]
        lastUpdatedValue = 0
        l, r = 0, len(snapshot) - 1
        while l <= r:
            mid = l + (r - l) // 2
            sid, val = snapshot[mid]
            if snap_id >= sid:
                lastUpdatedValue = val
                l = mid + 1
            else:
                r = mid - 1
        return lastUpdatedValue
            


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)