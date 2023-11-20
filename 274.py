import numpy as np

def hIndex(citations):
    citations.sort(reverse=True)
    indices = np.arange(1,len(citations)+1)
    diff = np.array(citations)-indices
    try:
        return(np.argmin(diff[diff>=0])+1)
    except ValueError:
        return(0)

def test_0():
    citations = [3,0,6,1,5]
    assert hIndex(citations) == 3 

def test_1():
    citations = [1,3,1]
    assert hIndex(citations) == 1

def test_2():
    citations = [0]
    assert hIndex(citations) == 0
    
if __name__ == '__main__':
    test_0()
    test_1()