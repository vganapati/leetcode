import math 

def minOperations(k):
    num_increases = 0
    num_duplicates = math.ceil(k/(1+num_increases) - 1)
    current_operations = num_increases + num_duplicates
    previous_operations = current_operations # dummy value to start loop
    while current_operations <= previous_operations: # stop loop when the number of operations starts increasing
        previous_operations = current_operations
        num_increases += 1
        num_duplicates = math.ceil(k/(1+num_increases) - 1)
        current_operations = num_increases + num_duplicates
    return previous_operations

def test_0():
    k = 11
    assert minOperations(k) == 5

def test_1():
    k = 1
    assert minOperations(k) == 0

if __name__ == "__main__":
    test_0()
    test_1()