class TimeMap:

    def __init__(self):
        self.keyValues = {} #{key:[value]}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keyValues.keys():
            self.keyValues[key][0].append(timestamp)
            self.keyValues[key][1].append(value)
        else:
            self.keyValues[key] = [[timestamp], [value]]


    def binarySearch(self, target, timestamp, values):

        keys = timestamp
        l, r = 0, len(keys) - 1
        highestTillNow = ""
        while l <= r:
            m = (l + r) //2

            if keys[m] < target:
                l = m + 1
                highestTillNow = m
            elif keys[m] > target:
                r = m - 1
            else:
                return values[m]
        if highestTillNow == "":
            return ""
        return values[highestTillNow]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.keyValues.keys():
            timestampValues = self.keyValues[key]
        else:
            return ""
        # what if values is null???
        higestVal = self.binarySearch(timestamp, timestampValues[0], timestampValues[1])
        if higestVal == "":
            return ""
        return higestVal

# Your TimeMap object will be instantiated and called as such:
# timeMap = TimeMap()
# timeMap.set("ctondw","ztpearaw",1)
# timeMap.set("vrobykydll","hwliiq",2)
# timeMap.set("gszaw","ztpearaw",3)
# timeMap.set("ctondw","gszaw",4)
# print(timeMap.get("gszaw",5))
# print(timeMap.get("ctondw",6))
# print(timeMap.get("ctondw",6))
# print(timeMap.get("ctondw",6))
# print(timeMap.get("gszaw",5))
# print(timeMap.get("gszaw",5))


# timeMap = TimeMap()
# timeMap.set("love","high",10)
# timeMap.set("love","low",20)
# print(timeMap.get("love",5))

timeMap = TimeMap()
timeMap.set("a","bar",1)
timeMap.set("x","b",3)
print(timeMap.get("b",3))