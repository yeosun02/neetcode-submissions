class TimeMap:

    def __init__(self):
        self.key_ind = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_ind[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_ind:
            return ""

        ind_ls = self.key_ind[key]
        l, r = 0, len(ind_ls) - 1
        while l < r:
            m = (r + l) // 2
            if ind_ls[m][0] <= timestamp:
                if ind_ls[m + 1][0] > timestamp:
                    return ind_ls[m][1]
                l = m + 1
            else:
                r = m - 1

        return ind_ls[l][1] if ind_ls[l][0] <= timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)