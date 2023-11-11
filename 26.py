def removeDuplicates(nums):
    previous_num = nums[0]

    remove_inds = []
    for ind,num in enumerate(nums[1:]):
        if nums[ind+1]==previous_num:
            remove_inds.append(ind+1)
        else:
            previous_num = nums[ind+1]
    for i in range(len(remove_inds)):
        del nums[remove_inds[len(remove_inds)-1-i]]
    
    k = len(nums)
    return k

removeDuplicates([1,1,2])