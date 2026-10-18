class TimeMap:

    def __init__(self):
        self.storage = {}  

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        arr = self.storage.get(key, [])
        low = 0 
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid][1] <= timestamp:
                result = arr[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return result