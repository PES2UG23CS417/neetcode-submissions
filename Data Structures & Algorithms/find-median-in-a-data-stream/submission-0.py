class MedianFinder:

    def __init__(self):
        self.res = []

    def addNum(self, num: int) -> None:
        self.res.append(num)
        self.res.sort()

    def findMedian(self) -> float:
        n = len(self.res)

        if n%2:
            return self.res[n//2]
        else:
            return (self.res[n//2] + self.res[n//2 - 1])/2