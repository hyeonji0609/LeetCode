class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_cost = [0] * len(cost)
        
        for i in range(2): # 2까지는 리스트에 담아줌
            total_cost[i] = cost[i]
        
        for i in range(2, len(cost)):
            total_cost[i] = cost[i] + min(total_cost[i-1], total_cost[i-2]) # 항상 가장 최선을 선택했다고 가정
 
        return min(total_cost[-1], total_cost[-2])
    
"""
Runtime: 51 ms
Memory Usage: 16.8 MB
"""