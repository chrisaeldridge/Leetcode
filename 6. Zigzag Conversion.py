from itertools import chain
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if len(s) in (0,1) or numRows in (0,1) or numRows >= len(s):
            return s
        
        ziglist = [[] for i in range(numRows)]
        irow = 0
        vertdir = 1
        for c in s:
            ziglist[irow].append(c)

            if irow == 0:
                vertdir = 1
            elif irow == (numRows - 1):
                vertdir = -1
            
            irow += vertdir

        return ''.join(list(chain.from_iterable(ziglist)))

print(f'answer = {Solution().convert(s="PAYPALISHIRING",numRows=3)}')
print("PAHNAPLSIIGYIR")

print(f'answer = {Solution().convert(s="PAYPALISHIRING",numRows=4)}')
print("PINALSIGYAHRPI")