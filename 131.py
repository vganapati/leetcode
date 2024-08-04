"""
Palindrome Partitioning
"""
import functools

def partition(s):
    if len(s) == 1:
        return [s]
    
    all_palindromes = []
    def dfs(s):
        max_partitions = len(s)-1
        all_partitions = [[0], [1]]
        while len(all_partitions)>0:
            if len(all_partitions[-1])==max_partitions:
                palindrome_partition = check_full_palindrome(s, all_partitions[-1])
                if palindrome_partition is not None:
                    all_palindromes.append(palindrome_partition)
                all_partitions.pop()
            else:
                all_partitions[-1].append(0)
                all_partitions.append(all_partitions[-1][:-1] + [1])
    
    def check_full_palindrome(s, partition_i):
        palindrome_partition = []
        current_str = s[0]
        for ind, character in enumerate(s[1:]):
            if partition_i[ind]:
                current_str += character
            else:
                if check_palindrome(tuple(current_str)):
                    palindrome_partition.append(current_str)
                    current_str = character
                else:
                    return None
        if check_palindrome(tuple(current_str)):
            palindrome_partition.append(current_str)
        else:
            return None
        return palindrome_partition
            

    @functools.cache
    def check_palindrome(partition_candidate):
        if partition_candidate[0:len(partition_candidate)//2] == partition_candidate[::-1][0:len(partition_candidate)//2]:
            return True
        else:
            return False
    
    dfs(s)
    return all_palindromes





def test_0():
    s = "aab"
    print(partition(s))

def test_1():
    s = "a"
    print(partition(s))

if __name__ == '__main__':
    test_0()
    test_1()
