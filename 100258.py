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
    test_0()
    test_1()
    test_2()
    test_3()