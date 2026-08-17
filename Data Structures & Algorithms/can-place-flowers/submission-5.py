class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = 0
        if n == 0:
            return True
        elif len(flowerbed) == 1:
            if n == 1 and flowerbed[0] == 0:
                return True
            else:
                return False
        elif len(flowerbed) == 2:
            count = 0
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                count += 1
                if count == n:
                    return True
                return False
        else:
            count = 0
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                count += 1
                flowerbed[0] = 1
                if count == n:
                    return True

            for i in range(1, len(flowerbed) - 1):
                if flowerbed[i] == 0:
                    if flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                        flowerbed[i] = 1
                        count += 1
                        if count == n:
                            return True
            i += 1
            if count < n:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    count += 1
                    if count == n:
                        return True
            return False
