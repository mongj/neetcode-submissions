class MyHashMap:

    def __init__(self):
        self.hashmap = dict()

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value
        print(f"inserting key: {key} value: {value}. After: {self.hashmap}")

    def get(self, key: int) -> int:
        try:
            print(f"getting key: {key} value: {self.hashmap[key]}")
            return self.hashmap[key]
        except KeyError:
            return -1

    def remove(self, key: int) -> None:
        try:
            del self.hashmap[key]
            print(f"removing key: {key}. After: {self.hashmap}")
        except:
            pass


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)