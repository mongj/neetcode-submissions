class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        message = (value, timestamp)
        if key in self.store:
            self.store[key].append(message)
        else:
            self.store[key] = [message]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store:
            return ""
        
        messages = self.store[key]
        low, high = 0, len(messages) - 1
        while low < high:
            mid = low + (high - low) // 2 + 1
            if messages[mid][1] > timestamp:
                high = mid - 1
            else:
                low = mid
        return messages[low][0] if messages[low][1] <= timestamp else ""
