from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.nums.sort(reverse=True)
        self.k = k

    def add(self, val: int) -> int:
        k_value = None
        inserted = False
        i=0
        if len(self.nums) == 0:
            self.nums.insert(0, val)
        else:
            while i < len(self.nums):
                if self.nums[i] <= val and not (inserted):
                    self.nums.insert(i, val)
                    inserted = True
                    break
                i+=1
        if inserted == False:
            self.nums.append(val)

        i = 0
        while i < len(self.nums):
            if i == self.k - 1:
                k_value = self.nums[i]
                break
            i+=1
        return k_value

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(3,[4,5,8,2])

# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(2,[0])
print(obj.add(-1))