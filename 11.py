import functools

def maxArea_0(height):
    if len(height) == 1:
        return 0
    elif len(height) == 2:
        return min(height)
    else:
        full = min(height[0],height[-1])*(len(height)-1)# using endpoints
        if max(height[1:-1]) < min(height[0],height[-1]):
            return full
        elif height[0] > height[-1]:
            for pointer in range(2,len(height)):
                if height[len(height)-pointer]>height[-1]:
                    return max(full, maxArea(height[:len(height)-pointer+1]))
            return full
        elif height[0] < height[-1]:
            for pointer in range(1,len(height)-1):
                if height[pointer]>height[0]:
                    return max(full, maxArea(height[pointer:]))
            return full
        elif height[0] == height[-1]:
            flag = False
            for pointer in range(1,len(height)-1):
                if height[pointer]>height[0]:
                    left_pointer = pointer
                    flag = True
                    break
            for pointer in range(2,len(height)):
                if height[len(height)-pointer]>height[-1]:
                    right_pointer = len(height)-pointer
                    flag = True
                    break
            if flag:
                return max(full, maxArea(height[left_pointer:right_pointer+1]))
            else:
                return full


def maxArea(height):
    left_pointer = 0
    right_pointer = len(height)-1
    max_water = 0
    flag = True
    while left_pointer < right_pointer and flag:
        water = min(height[left_pointer],height[right_pointer])*(len(height[left_pointer:right_pointer]))
        if water > max_water:
            max_water = water
        flag = False
        if height[left_pointer] > height[right_pointer]:
            for pointer in range(2,len(height)-left_pointer):
                if height[len(height)-pointer]>height[right_pointer]:
                    right_pointer = len(height)-pointer
                    flag = True
                    break
        elif height[left_pointer] <= height[right_pointer]:
            for pointer in range(1,right_pointer):
                if height[pointer]>height[left_pointer]:
                    left_pointer = pointer
                    flag = True
                    break
    return max_water


def test_0():
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49

def test_1():
    assert maxArea([1,1]) == 1

def test_2():
    assert maxArea([2,3,4,5,18,17,6]) == 17

def test_3():
    assert maxArea([1,8,100,2,100,4,8,3,7]) == 200

if __name__ == "__main__":
    test_3()
    test_2()
    test_0()
    test_1()