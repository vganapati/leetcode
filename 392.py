def isSubsequence(s: str, t: str) -> bool:
    ind_t = 0
    ind_s = 0
    matches = 0
    while ind_t < len(t) and ind_s < len(s):
        if s[ind_s] == t[ind_t]:
            ind_s += 1
            matches += 1
        ind_t += 1
    
    if len(s) == matches:
        return True
    else:
        return False

def test_0():
    s = "abc"; t = "ahbgdc"
    assert isSubsequence(s, t) == True

if __name__ == '__main__':
    test_0()
    
        
