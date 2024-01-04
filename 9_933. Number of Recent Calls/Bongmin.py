class RecentCounter:

    def __init__(self):
        self.ls = [] # 핑 요청을 담을 리스트 생성
        
    def ping(self, t: int) -> int:
        min_ping = t-3000 # min 설정
        max_ping = t # max 설정

        # 핑 요청을 리스트에 append
        self.ls.append(t)
        # 사이에 있는 것을 세기
        cnt = 0
        for i in self.ls:
            if min_ping <= i <= max_ping:
                cnt += 1
        

        return cnt 

'''
runtime : 6759ms beats 5%...
memory : 22.74 beats 21.59%...
'''