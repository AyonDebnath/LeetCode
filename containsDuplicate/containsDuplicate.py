def containsDuplicate(nums) -> bool:
    nums_dict = {}
    for i in nums:
        if i in nums_dict:
            return True
        else:
            nums_dict[i] = '_'
    return False

print(containsDuplicate([1,2,3,1]))
