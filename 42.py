import numpy as np

def trap_0(height):
    height = np.array(height)
    water = 0
    while len(np.nonzero(height)[0]):
        height_bool = np.array(height).astype(bool)
        start_ind = np.nonzero(height_bool)[0][0]
        end_ind = np.nonzero(height_bool)[0][-1]
        water += (end_ind-start_ind-np.sum(height_bool)+1)
        height[height>=1] -= 1
    return water

def trap_1(height):
    height = np.array(height)
    
    heights = np.arange(0,np.max(height))
    heights_repeat = np.repeat(np.expand_dims(height,axis=1), np.max(height),axis=1)
    heights_repeat = heights_repeat - heights
    heights_repeat[heights_repeat<0] = 0
    heights_repeat[heights_repeat>0] = 1
    height_sum = np.sum(heights_repeat, axis=0)
    height_starts = np.argmax(heights_repeat, axis=0)
    height_stops = np.argmax(np.flipud(heights_repeat), axis=0)
    waters = len(height)-height_starts-1-height_stops-1-height_sum+2
    return np.sum(waters)

def trap_2(height,step=1):
    height = np.array(height)
    if not(len(np.nonzero(height)[0])):
        return 0
    
    lowest_height = np.min(height[height>0])
    lowest_height_ind = np.nonzero(height>=lowest_height)[0]
    base_height = lowest_height_ind[-1]-lowest_height_ind[0]-1-np.sum(height>=lowest_height)+2
    base_height *= lowest_height
    height -= lowest_height
    height[height<0]=0
    water = 0
    for i in range(0,np.max(height),step):
        height_i = np.copy(height)
        height_i = height_i - i
        height_i[height_i>step]=step
        water += trap_1(height_i)
    return water + base_height

def trap_3(height):
    height = np.array(height)
    lowest_height = np.min(height[height>0])
    lowest_height_ind = np.nonzero(height>=lowest_height)[0]
    base_height = lowest_height_ind[-1]-lowest_height_ind[0]-1-np.sum(height>=lowest_height)+2
    base_height *= lowest_height
    height -= lowest_height
    height[height<0]=0   
    
    water = trap_helper(height)
    return water + base_height


def trap_helper(height):
    if len(height)<=1:
        return 0
    sorted_height = np.argsort(height)

    high_0_ind = sorted_height[-1]
    high_1_ind = sorted_height[-2]
    if np.all(height[sorted_height]==height) or np.all(height[sorted_height]==np.flip(height)):
        return 0
    del sorted_height
    high_0 = height[high_0_ind]
    high_1 = height[high_1_ind]

    water = high_1*(np.abs(high_1_ind-high_0_ind)-1)-\
        np.sum(height[min(high_0_ind,high_1_ind)+1:max(high_0_ind,high_1_ind)])
    if min(high_0_ind,high_1_ind)==0 and max(high_0_ind,high_1_ind)==len(height)-1:
        return water
    elif max(high_0_ind,high_1_ind) >= len(height)-2:
        return water + trap_helper(height[:min(high_0_ind,high_1_ind)+1]) 
    elif min(high_0_ind,high_1_ind)<=1:
        return water + trap_helper(height[max(high_0_ind,high_1_ind):])
    else:
        return water + trap_helper(height[max(high_0_ind,high_1_ind):]) +\
            trap_helper(height[:min(high_0_ind,high_1_ind)+1]) 

def find_nearest_high(current_ind, height):
    # find pointer_1_ind
    pointer_1_ind = current_ind
    current_height = height[current_ind]
    for ind,h in enumerate(height[current_ind+1:]):
        if h>=current_height:
            pointer_1_ind = ind + current_ind + 1
            current_height = h
    return pointer_1_ind
    
def trap(height):
    pointer_0_ind = 0 # point in the past at the greatest height
    pointer_1_ind = 0 # point in the future at the greatest height
    water = 0
    for ind,h in enumerate(height):

        # update pointer_0_ind if current point is the same or higher
        if h>=height[pointer_0_ind]:
            pointer_0_ind = ind

        # update pointer_1_ind if we have reached or exceeded the pointer
        if ind >= pointer_1_ind:
            pointer_1_ind = find_nearest_high(ind, height)
        water += min(height[pointer_1_ind], height[pointer_0_ind])-h
    return water

def test_0():
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

def test_1():
    assert trap([4,2,0,3,2,5]) == 9

def test_2():
    assert trap([0,7,1,4,6]) == 7

def test_3():
    assert trap([2,8,5,5,6,1,7,4,5]) == 12

if __name__ == '__main__':
    test_0()
    test_1() 
    test_2()
    test_3()