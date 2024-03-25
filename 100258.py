import heapq

def mostFrequentIDs(nums, freq):
    ans = []
    id_heap = [] # top of heap is lowest freq
    id_dict = {} # key is ID, value is freq
    for ind, (num, freq) in enumerate(zip(nums, freq)):
        try:
            id_dict[num] += freq
        except KeyError:
            id_dict[num] = freq
        heapq.heappush(id_heap, [-id_dict[num], num])
        flag = True
        while flag:
            freq_i = -id_heap[0][0]
            id_i = id_heap[0][1]
            if id_dict[id_i] != freq_i:
                heapq.heappop(id_heap)
            else:
                flag = False

        ans.append(freq_i)
    return ans

def mostFrequentIDs_0(nums, freq):
    ans = []
    id_ranked_list_id = [] # least frequent in beginning
    id_ranked_list_freq = []
    id_dict = {}
    for ind, (num, freq) in enumerate(zip(nums, freq)):
        try:
            id_dict[num] += freq
            # check if you need to change position
            ind_ranked_list = id_ranked_list_id.index(num)
            if (ind_ranked_list != 0 and id_ranked_list_freq[ind_ranked_list-1] > id_dict[num]) or (len(id_ranked_list_id)!= ind_ranked_list+1 and id_ranked_list_freq[ind_ranked_list+1] < id_dict[num]):
                id_ranked_list_id.pop(ind_ranked_list)
                id_ranked_list_freq.pop(ind_ranked_list)
                reinsert = True
            else:
                id_ranked_list_freq[ind_ranked_list] = id_dict[num]
                reinsert = False
        except KeyError:
            id_dict[num] = freq
            reinsert = True

        if reinsert:
            # insert into id_ranked_list_id and id_ranked_list_freq
            # binary search to place to insert
            insert_ind = findInsertionPoint(id_ranked_list_freq, id_dict[num], 0)
            id_ranked_list_id.insert(insert_ind, num)
            id_ranked_list_freq.insert(insert_ind, id_dict[num])
        ans.append(id_ranked_list_freq[len(id_ranked_list_freq)-1])
    return ans
        
def findInsertionPoint(id_ranked_list_freq, freq, start_ind):
    if len(id_ranked_list_freq) == 0:
        return start_ind
    elif len(id_ranked_list_freq) == 1:
        if freq <= id_ranked_list_freq[0]:
            return start_ind
        else:
            return start_ind+1
    else:
        if id_ranked_list_freq[len(id_ranked_list_freq)//2] > freq:
            return findInsertionPoint(id_ranked_list_freq[:len(id_ranked_list_freq)//2], freq, start_ind)
        else:
            return findInsertionPoint(id_ranked_list_freq[len(id_ranked_list_freq)//2:], freq, start_ind+len(id_ranked_list_freq)//2)
        
def test_0():
    nums = [2,3,2,1]; freq = [3,2,-3,1]
    assert mostFrequentIDs(nums, freq) == [3,3,2,2]

def test_1():
    nums = [5,5,3]; freq = [2,-2,1]
    assert mostFrequentIDs(nums, freq) == [2,0,1]

def test_2():
    nums = [6,3,6]; freq = [5,5,4]
    assert mostFrequentIDs(nums, freq) == [5,5,9]

def test_3():
    nums = [7,8,8]; freq = [5,1,5]
    assert mostFrequentIDs(nums, freq) == [5,5,6]

if __name__ == "__main__":
    test_3()
    test_1()
    test_0()
    test_2()