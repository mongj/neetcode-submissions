class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = {}
        self.lastSnapshotId = -1

    def set(self, index: int, val: int) -> None:
        #print("set", index, val)
        targetSnapshotId = self.lastSnapshotId + 1
        if targetSnapshotId not in self.snapshots:
            self.snapshots[targetSnapshotId] = []
        self.snapshots[targetSnapshotId].append((index, val))

    def snap(self) -> int:
        #print(f"snap: {self.lastSnapshotId} -> {self.lastSnapshotId + 1}")
        self.lastSnapshotId += 1
        return self.lastSnapshotId

    def get(self, index: int, snap_id: int) -> int:
        if snap_id > self.lastSnapshotId:
            #print("get (index: {index}, snap_id: {snap_id}) -> 0")
            return 0

        #print(self.snapshots)
        for sid in range(snap_id, -1, -1):
            if sid not in self.snapshots:
                continue
            for (sid, sval) in self.snapshots[sid][::-1]:
                if sid == index:
                    #print("get (index: {index}, snap_id: {snap_id}) -> {sval}")
                    return sval 

        #print("get (index: {index}, snap_id: {snap_id}) -> 0")
        return 0
            


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)