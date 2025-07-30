class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
         self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        pairs = self.store[key]
        left, right = 0, len(pairs) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res   

    """
    again, it is going to search the polarizing value, so it's good strategy to use the binary search
    每次看 mid 的 timestamp 是否 ≤ target
    如果是，表示可以當作暫時答案，並嘗試往右邊找更接近的 timestamp
    """     
