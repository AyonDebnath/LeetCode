def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    while(i<len(nums)):
        j= i+1
        while(j<len(nums)):
            if(nums[i]+nums[j] == target) :
                return([i, j])
            j+=1
        i+=1
    

def main() :
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([3,2,4], 6))
    print(twoSum([3,3], 6))

main()