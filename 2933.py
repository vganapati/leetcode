import numpy as np

def findHighAccessEmployees(access_times):
    high_access = []
    access_times_dict = {}
    for name,time in access_times:
        # convert time to base 10
        time = int(time[:2])*60 + int(time[2:])
        try:
            access_times_dict[name].append(time)
        except KeyError:
            access_times_dict[name]=[time]
    for key in access_times_dict.keys():
        value = access_times_dict[key]
        if len(value)>=3:
            value.sort()
            if np.any(np.convolve(value, [1,0,-1],'valid') < 60):
                high_access.append(key)
        else:
            pass
    return high_access
    
def test_0():
    access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]
    assert set(findHighAccessEmployees(access_times)) == set(["a"])

def test_1():
    access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]
    assert set(findHighAccessEmployees(access_times)) == set(["c","d"])

def test_2():
    access_times = [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]
    assert set(findHighAccessEmployees(access_times)) == set(["ab","cd"])

def test_3():
    access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]
    assert set(findHighAccessEmployees(access_times)) == set(["a"])

if __name__ == '__main__':
    test_0()
    test_1()
    test_2()
    test_3()
