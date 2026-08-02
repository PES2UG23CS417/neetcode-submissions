class Solution:
    def myPow(self, x: float, n: int) -> float:
        binary = ""
        if n < 0:
            x = 1/x
            n = -n

        if n == 0:
            binary = "0"
        else:
            while n > 0:
                binary = str(n%2) + binary
                n //= 2
        
        i = len(binary) - 1
        res = 1
        while i >= 0:
            if binary[i] == "1":
                res = res*x
            x *= x
            i -= 1
            
        return res