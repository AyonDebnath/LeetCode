class Solution:
    def productExceptSelf(self, nums):
        answer = []
        for i in range(len(nums)):
            # calculate the prefix
            if(i == 0):
                answer.append(1)
            else:
                answer.append(answer[i-1] * nums[i-1])

        suffix = 1
        # calculating the output
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix = nums[i] * suffix
        return answer


def main():
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))

main()