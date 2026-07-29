class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        f = []
        
        for bro in order:
            if bro in friends:
                f.append(bro)
        
        return f