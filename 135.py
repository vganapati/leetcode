def candy_0(ratings):
    candy_per_child = candy_helper(ratings)
    return sum(candy_per_child) 

def candy_helper(ratings):
    # return list of candy_per_child
    if len(ratings) == 1:
        return [1]
    elif len(ratings) == 2:
        if ratings[0] == ratings[1]:
            return [1,1]
        elif ratings[0]>ratings[1]:
            return [2,1]
        else:
            return [1,2]
    else:
        candy_per_child = candy_helper(ratings[:-1])
        if ratings[-1]>ratings[-2]:
            last_child = candy_per_child[-1] + 1
            candy_per_child.append(last_child)
        elif ratings[-1] == ratings[-2]:
            last_child = 1
            candy_per_child.append(last_child)
        elif ratings[-1]<ratings[-2]:
            last_child = 1
            candy_per_child.append(last_child)
            for ind in range(-2, -len(ratings)-1,-1):
                if ratings[ind]>ratings[ind+1] and candy_per_child[ind]<=candy_per_child[ind+1]:
                    candy_per_child[ind] += 1
                else:
                    break
        return candy_per_child

def candy(ratings):
    candy_per_child = [1]
    flag_ind = -1
    ind = 1
    while ind<len(ratings):
        if ratings[ind-1] < ratings[ind]:
            candy_per_child.append(candy_per_child[ind-1]+1)
            flag_ind = -1
            ind += 1
        elif ratings[ind-1] == ratings[ind]:
            candy_per_child.append(1)
            flag_ind = -1
            ind += 1
        elif ratings[ind-1] > ratings[ind]:
            candy = 1
            candy_per_child_2 = [candy]
            for ind_2 in range(ind, len(ratings)):
                if ratings[ind_2-1] > ratings[ind_2]:
                    candy_per_child_2.append(candy+1)
                    candy += 1
                    ind = ind_2+1
                else:
                    ind = ind_2
                    break
            candy_per_child_2.reverse()
            if candy_per_child_2[0]>candy_per_child[-1]:
                candy_per_child.pop()
            else:
                candy_per_child_2.pop(0)
            candy_per_child += candy_per_child_2
    return sum(candy_per_child)
            

def test_0():
    assert candy([1,0,2]) == 5

def test_1():
    assert candy([1,2,2]) == 4

def test_2():
    assert candy([1,3,2,2,1]) == 7

def test_3():
    assert candy([1,2,87,87,87,2,1]) == 13

def test_4():
    assert candy([1,3,4,5,2]) == 11

if __name__ == '__main__':
    test_4()
    test_3()
    test_2()
    test_0()
    test_1()