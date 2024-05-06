class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res_ls = [0] * len(cost) # 0 배열 만들기
        res_ls[0] = cost[0] # 0 배열 0번째는 cost 0번쨰
        res_ls[1] = cost[1] # 0 배열 1번째는 cost 1번째
        
        # 0 배열을 채워 나가는 걸로 생각 # 설명 필요
        for i in range(2,len(cost)):
            res_ls[i] = min((res_ls[i-2]+cost[i]), (res_ls[i-1]+cost[i]))
        return min(res_ls[-1],res_ls[-2])
    
'''
runtime : 44ms beats 97.09%
memory : 16.92 beats 17.42%
'''