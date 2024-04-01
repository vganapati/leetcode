import numpy as np
def minimumDistance_0(points):
    # which 2 points cause the maximum distance, and which one to remove?
    points = np.expand_dims(np.array(points),-1)
    point_dist_mat = np.sum(np.abs(np.repeat(points,len(points), axis=-1) - points.T), axis=1)
    point_0, point_1 = np.unravel_index(np.argmax(point_dist_mat), [len(points),len(points)])
    
    max_0 = removeAndFindMax(point_0, point_dist_mat, points)
    max_1 = removeAndFindMax(point_1, point_dist_mat, points)
    return np.min([max_0, max_1])

def removeAndFindMax(point_0, point_dist_mat, points):
    remove_0_vec = np.concatenate((np.arange(point_0), np.arange(point_0+1,len(points))), axis=0)
    max_0 = np.max(point_dist_mat[np.repeat(np.expand_dims(remove_0_vec,axis=1), len(points)-1,axis=1), np.repeat(np.expand_dims(remove_0_vec,axis=0), len(points)-1,axis=0)])
    return max_0

def minimumDistance_1(points):
    # which 2 points cause the maximum distance, and which one to remove?
    dist_list = []
    max_dist = 0
    possible_points = []
    for ind, point_0 in enumerate(points[:-1]):
        sub_dist_list = []
        for ind_1, point_1 in enumerate(points[ind+1:]):
            dist = abs(point_0[0]-point_1[0]) + abs(point_0[1]-point_1[1])
            sub_dist_list.append(dist)
            if dist > max_dist or dist == max_dist:
                if dist > max_dist:
                    possible_points = [ind, ind_1 + ind + 1]
                elif dist == max_dist:
                    possible_points.append(ind)
                    possible_points.append(ind_1 + ind + 1)
                max_dist = dist
        dist_list.append(sub_dist_list)
    
    minimum = 2*10**8
    for point in possible_points:
        max_val_0 = [max(l[0:point-ind-1]+l[point-ind:] + [0]) for ind,l in enumerate(dist_list[0:point])]
        max_val_1 = [max(l + [0]) for l in  dist_list[point+1:]]
        max_val = max(max_val_0 + max_val_1)
        if max_val < minimum:
            minimum = max_val
    return minimum


def minimumDistance(points):
    val, i, j = minimumDistance_helper(points)
    val_0, i_0, j_0 = minimumDistance_helper(points[:i] + points[i+1:])
    val_1, i_1, j_1 = minimumDistance_helper(points[:j] + points[j+1:])
    return min([val_0, val_1])

def minimumDistance_helper(points):
    max_sum, min_sum, max_diff, min_diff = -10**9, 10**9, -10**9, 10**9
    max_sum_ind, min_sum_ind, max_diff_ind, min_diff_ind = None, None, None, None
    for ind,point in enumerate(points):
        sum = point[0] + point[1]
        diff = point[0] - point[1]

        if sum >= max_sum:
            max_sum = sum
            max_sum_ind = ind
        if sum <= min_sum:
            min_sum = sum
            min_sum_ind = ind
        
        if diff >= max_diff:
            max_diff = diff
            max_diff_ind = ind
        if diff <= min_diff:
            min_diff = diff
            min_diff_ind = ind
    if max_sum - min_sum > max_diff - min_diff:
        return max_sum - min_sum, max_sum_ind, min_sum_ind
    else:
        return max_diff - min_diff, max_diff_ind, min_diff_ind

def test_0():
    points = [[3,10],[5,15],[10,2],[4,4]]
    assert minimumDistance(points) == 12

def test_1():
    points = [[1,1],[1,1],[1,1]]
    assert minimumDistance(points) == 0

def test_2():
    points = [[100000000,100000000],[100000000,100000000],[100000000,100000000],[100000000,100000000],[100000000,100000000],[100000000,100000000],[100000000,100000000],[100000000,100000000],[100000000,100000000],[100000000,100000000]]
    assert minimumDistance(points) == 0

if __name__ == '__main__':
    test_2()
    test_0()
    test_1()