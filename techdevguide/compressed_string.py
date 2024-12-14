"""
https://techdevguide.withgoogle.com/resources/former-interview-question-compression-and-decompression/#!
https://leetcode.com/problems/decode-string/submissions/1478258556/
"""

def decompress(compressed: str) -> str:
    digit = ""
    string = ""
    ind = 0
    while ind<len(compressed):
        char = compressed[ind]
        if char.isdigit():
            digit += char
            ind += 1
        elif char.islower():
            string += char
            ind += 1
        elif char == "[":
            new_string, new_ind = decompress(compressed[ind+1:])
            if digit == "":
                pass
            else:
                string += int(digit)*new_string
            ind += new_ind + 1
            digit = ''
        elif char == "]":
            return string, ind+1
    return string


assert decompress("2[3[a]b]") == "aaabaaab"
assert decompress("3[abc]4[ab]c") == "abcabcabcababababc"
assert decompress("10[a]") == "aaaaaaaaaa"
assert decompress("a[]b") == "ab"
assert decompress("a[abc]b") == "ab"
assert decompress("0[abc]") ==""