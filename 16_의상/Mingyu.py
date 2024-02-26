def solution(clothes):
    # 의상 category 별로 의상 갯수를 맵핑할 closet_map 초기화
    closet_map = {}
    # clothes를 순회하며, category를 count하여 closet_map에 할당
    for cloth, category in clothes:
        if category in closet_map:
            closet_map[category] += 1
        else:
            closet_map[category] = 1
    
    # category 별로 가능한 의상 조합 수(안입을 때 포함) 계산
    combination = 1
    for category in closet_map:
        combination *= (closet_map[category] + 1) # 각 category 내의 의상을 하나도 안고를 경우(+1)
    return combination-1 # 전체 category를 모두 안고를 경우 제외(-1)