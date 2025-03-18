class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s  

        a = ""  
        n = numRows

        for i in range(n):
            incr = 2 * (n - 1)
            for j in range(i, len(s), incr):
                a += s[j]  
                if i > 0 and i < n - 1 and (j + incr - 2 * i) < len(s):
                    a += s[j + incr - 2 * i]

        return a
sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))  
print(sol.convert("PAYPALISHIRING", 4)) 
print(sol.convert("A", 1))  
