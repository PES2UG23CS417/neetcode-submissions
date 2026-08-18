class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        new_list = []
        for i in range(len(position)):
            new_list.append([position[i], speed[i]])
        
        new_list.sort(key = lambda i:i[0])

        for pair in range(len(new_list)-1,-1,-1):
            if not stack:  stack.append(new_list[pair])
            else:
                d1 = (target - stack[-1][0])/stack[-1][1]
                d2 = (target - new_list[pair][0])/new_list[pair][1]
                if d2 > d1:
                    stack.append(new_list[pair])
        return len(stack)