class Solution:
    def reverseBits(self, n: int) -> int:
        binary_rep = bin(n)
        print(binary_rep)
        binary_rep = binary_rep[2::]
        rev = binary_rep[::-1]
        print(rev)
        while(len(rev) != 32):
            rev = rev + "0"
        print(rev)
        return int(rev, 2)