class TimeMap:

    def __init__(self):
        self.tmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        a = self.tmap.get(key, [])
        a.append((value, timestamp))
        self.tmap[key] = a

    def get(self, key: str, timestamp: int) -> str:
        a = self.tmap.get(key, [])
        l = 0
        r = len(a) - 1
        latestSeen = ("", -1)
        while l <= r:
            m = l + (r - l) // 2
            if a[m][1] == timestamp:
                return a[m][0]
            elif a[m][1] < timestamp:
                if a[m][1] > latestSeen[1]:
                    latestSeen = a[m]
                l = m + 1
            else:
                r = m - 1
        return latestSeen[0]
