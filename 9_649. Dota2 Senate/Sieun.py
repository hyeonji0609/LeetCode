class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = list(senate)  # 'senate' 문자열을 리스트로 변환하여 각 상원의원을 나타냄

        while queue and (not all(q == queue[0] for q in queue)): # 모든 상원의원이 같은 당에 속하지 않는 동안 반복
            temp = queue.pop(0)  # 큐의 첫 번째 상원의원을 제거하고 'temp'에 저장

            for i in range(len(queue)):
                if temp != queue[i]:
                    # 'temp' (현재 처리 중인 상원의원)와 다른 당의 상원의원을 찾음
                    queue.pop(i)  # 상대 당의 상원의원을 제거
                    break

            queue.append(temp)  # 처리된 상원의원을 큐의 끝에 다시 추가

        # 반복문이 끝나면, 한 당의 모든 상원의원이 제거되었음을 의미
        if queue[0] == "R":
            return "Radiant"  # 첫 번째 상원의원이 Radiant 당이면, Radiant가 승리
        else:
            return "Dire"  # 그렇지 않으면 Dire가 승리

"""
Runtime 995 ms
Memory 17.54 MB
"""