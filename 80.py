def removeDuplicates(nums):
    num_0 = nums[0]
    try:
        num_1 = nums[1]

        remove_inds = []
        ind = 2
        while ind < len(nums):
            num_2 = nums[ind]
            if num_0 == num_1 == num_2:
                del nums[ind]
            else:
                ind += 1
                num_0 = num_1
                num_1 = num_2
        print(nums)
    except IndexError:
        pass
    return len(nums)

print(removeDuplicates([1]))