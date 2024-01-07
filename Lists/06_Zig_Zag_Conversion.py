

class Solution:

    def convert(self, s: str, numRows: int) -> str:

        splits = list(range(numRows, 1, -1))
        rowarr = [""] * numRows
        col_id = 0
        i = 0
        counter = 0
        while i < len(s):
            col_id = splits[counter % len(splits)] if len(splits) > 0 else 1
            if col_id == numRows:
                end = min(len(s)-i, numRows)
                for k in range(end):
                    rowarr[k] += s[i+k]
                i += numRows
            else:
                rowarr[col_id-1] += s[i]
                i += 1
            counter += 1
        
        
        op_string = "".join(rowarr)
        return op_string

        
                    

        


            

soln = Solution()
s = "PAYPALISHIRING"
numRows = 4
print(soln.convert(s, numRows))

soln = Solution()
s = "A"
numRows = 1
print(soln.convert(s, numRows))