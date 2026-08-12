import os
os.system('cls')

def removeDuplicates(nums):

    if len(nums) == 0:
        return 0

    count = 1

    for i in range(1, len(nums)):

        if nums[i] != nums[i-1]:
            nums[count] = nums[i]

            count +=1

    return count


nums = [0,1,1,2,2]
print(removeDuplicates(nums))