class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        # binary search to find the tuple with the largest timestamp <= timestamp
        timestamps = self.store[key]
        l, r = 0, len(timestamps)
        while l <= r:
            mid = l + (r - l) // 2
            if timestamps[mid][1] > timestamp:
                r = mid - 1
            elif mid + 1 >= len(timestamps) or timestamps[mid + 1][1] > timestamp:
                return timestamps[mid][0]
            else:
                l = mid + 1
        return ""
