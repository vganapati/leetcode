def rotate(nums,k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k%len(nums)
    first = nums[len(nums)-k:]
    last = nums[:len(nums)-k]
    nums[:k] = first
    nums[k:] = last

    print(nums)

nums = [1,2,3,4,5,6,7]
k = 3
# rotate(nums,k)

rotate([1],1)