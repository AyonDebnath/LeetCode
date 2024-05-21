class Solution:
    def productExceptSelf(self, nums):
        answer = []
        prefix = []
        suffix = []
        for i in range(len(nums)):
            if(i == 0):
                prefix.append(1)
            else:
                prefix.append(prefix[i-1] * nums[i-1])

        for j in range(len(nums)-1, -1, -1):
            if j == (len(nums) - 1):
                suffix.append(1)
            else:
                suffix.insert(0, (suffix[0] * nums[j+1]))
        for i in range(len(nums)):
            answer.append(prefix[i] * suffix[i])
        return answer


def main():
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))

main()