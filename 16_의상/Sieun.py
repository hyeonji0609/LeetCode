def solution(clothes):
    hashclothes = dict()
    answer = 1
    
    for i in range(len(clothes)):
        if clothes[i][1] not in hashclothes:
            hashclothes[clothes[i][1]] = 1
        hashclothes[clothes[i][1]] += 1
    
    for j in list(hashclothes.values()):
        answer *= j
        
    return answer-1