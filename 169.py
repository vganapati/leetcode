def majorityElement(nums):
    threshold = len(nums)//2
    appearances_dict = {}

    for num in nums:
        try:
            appearances_dict[num] += 1
        except KeyError:
            appearances_dict[num] = 1
        
        if appearances_dict[num] > threshold:
            return num
        
print(majorityElement([3,2,3]))
