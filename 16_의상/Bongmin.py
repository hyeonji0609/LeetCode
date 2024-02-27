def solution(clothes):
    # =============================
    # 의상들 dict 형태로 만들어주기
    # 의상들은 모두 다르므로 숫자가 들어가게끔 만들었음!
    clothes_dict = {}
    for i in clothes:
        if i[1] not in clothes_dict.keys():
            clothes_dict[i[1]] = [0] # 키가 없다면 만들고 [0]을 집어넣기
        else:
            clothes_dict[i[1]].append(clothes_dict[i[1]][-1]+1) # 항상 마지막 숫자 +=1 하도록 설계
    # =============================
    # 키 값들의 len+1 해서 모두 곱해준 후 
    answer = 1
    for i in clothes_dict.values():
        answer *= len(i)+1
    
    # -1하는 이유는 모든 의상 종류에서 안입는 경우의 수를 빼주어야하기 때문
    return answer-1