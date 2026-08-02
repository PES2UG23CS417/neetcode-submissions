class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for j in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for k in range(len(res[-1]) + 1):
                row.append(temp[k] + temp[k+1])
            res.append(row)
        return res
        