def medianOfUniquenessArray(nums):
    min_k = 0
    max_k = len(nums)

    if len(nums) == 1:
        return 1
    
    def medianOfUniquenessArray(min_k, max_k):
        median_array_len = (len(nums) + 1) * (len(nums)//2) + (len(nums) % 2) * ((len(nums)+1)//2)
        median_ind = median_array_len//2 - 1 + (median_array_len % 2)
        k = min_k + (max_k - min_k)//2

        while True:
            num_above = allAbove(k)
            num_below = median_array_len - num_above
            if k + 1 > len(nums):
                num_above_plus_one = 0 
            else:
                num_above_plus_one = allAbove(k+1)

            if median_ind >= num_below and median_ind < median_array_len - num_above_plus_one:
                return k
            elif num_above > num_below:
                min_k = k
                return medianOfUniquenessArray(min_k, max_k)
            else:
                max_k = k
                return medianOfUniquenessArray(min_k, max_k)

    def allAbove(k):
        pointer_0 = 0
        pointer_1 = k # not included in the subarray
        distinct_dict = {}
        for num in nums[pointer_0:pointer_1]:
            try:
                distinct_dict[num] += 1
            except KeyError:
                distinct_dict[num] = 1

        num_above = 0
        pointer_1_flag = True
        while pointer_0 <= len(nums)-k and pointer_1_flag:
            if len(distinct_dict.keys()) >= k:
                num_above += 1 + len(nums) - pointer_1

                # move pointer_0
                distinct_dict[nums[pointer_0]] -= 1
                if distinct_dict[nums[pointer_0]] == 0:
                    del distinct_dict[nums[pointer_0]]
                pointer_0 += 1
            else:
                # move pointer_1
                if pointer_1 >= len(nums):
                    pointer_1_flag = False
                else:
                    try: 
                        distinct_dict[nums[pointer_1]] += 1
                    except KeyError:
                        distinct_dict[nums[pointer_1]] = 1
                    pointer_1 += 1
        return num_above

    return medianOfUniquenessArray(min_k, max_k)

def test_0():
    nums = [1,2,3]
    assert medianOfUniquenessArray(nums) == 1

def test_1():
    nums = [3,4,3,4,5]
    assert medianOfUniquenessArray(nums) == 2

def test_2():
    nums = [4,3,5,4]
    assert medianOfUniquenessArray(nums) == 2

def test_3():
    nums = [1]
    assert medianOfUniquenessArray(nums) == 1

def test_4():
    nums = [52,50,50]
    assert medianOfUniquenessArray(nums) == 1

def test_5():
    nums = [91,64,76,18,61,55,46,93,65,99]
    assert medianOfUniquenessArray(nums) == 4

if __name__ == '__main__':
    test_0()
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    
    