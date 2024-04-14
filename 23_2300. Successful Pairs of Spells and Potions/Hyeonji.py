class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        output = []
        potions.sort()
        
        # binary search        
        for s in spells:
            start = 0
            end = len(potions) - 1
            smallestIdx = len(potions)
            
            while start <= end:
                mid = (start + end) // 2
                
                if potions[mid] * s >= success:
                    smallestIdx = mid # smallestIdx 갱신
                    end = mid - 1
                    
                else:
                    start = mid + 1
            
            if smallestIdx == len(potions): # 만약에 smallestIdx가 갱신이 안된다면
                output.append(0)
            else:
                output.append(len(potions) - smallestIdx)
            
        return output
"""
Runtime: 1310 ms
Memory Usage: 39.7 MB
"""

# Time Limit Exceeded
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        output = []
        
        for s in spells:
            mul_potions = list(map(lambda x: x * s, potions))
            success_list = list(filter(lambda x: x >= success, mul_potions))
            output.append(len(success_list))
        
        return output