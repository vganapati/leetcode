def minEnd(n, x):
    add_number = list(reversed("{0:b}".format(n-1)))
    final_val = list(reversed("{0:b}".format(x)))
    add_number_ind = 0
    final_val_ind = 0
    init_len = len(final_val)
    while add_number_ind<len(add_number):
        if final_val_ind < init_len:
            if final_val[final_val_ind] == '0':
                final_val[final_val_ind] = add_number[add_number_ind]
                add_number_ind += 1
            final_val_ind += 1
        else:
            final_val.append(add_number[add_number_ind])
            add_number_ind += 1

    final_val = "".join(list(reversed(final_val)))
    return int(final_val,2)

def test_0():
    n = 3; x = 4
    assert minEnd(n, x) == 6

def test_1():
    n = 2; x = 7
    assert minEnd(n, x) == 15

if __name__ == '__main__':
    test_0()
    test_1()