class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate) # 리스트로 바꿔주기

        # 돌릴 동안에
        while True:
            # 맨 처음이 R이라면
            if senate[0] == "R":
                try:
                    # D를 찾아 없애버리고
                    senate.pop(senate.index("D"))
                    # 맨 처음인 R을 pop해서 뒤에다가 추가하기
                    senate.append(senate.pop(0))
                except:
                    break
            # 맨 처음이 D라면
            else:
                try:
                    # R을 찾아 없애버리고
                    senate.pop(senate.index("R"))
                    # 맨 처음인 D를 pop해서 뒤에다가 추가하기
                    senate.append(senate.pop(0))
                except:
                    break
            
        return "Radiant" if senate[0] =="R" else "Dire"
                
                
            
            
            