def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    while(i<len(nums)):
        toFind = target - nums[i]
        try :
            result = nums.index(toFind, i+1)
            return [i, result]
        except ValueError:
            i+=1

def main() :
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([3,2,4], 6))
    print(twoSum([3,3], 6))

main()