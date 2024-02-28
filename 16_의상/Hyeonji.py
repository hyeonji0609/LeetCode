def solution(clothes):
    hashtable = {}
    answer = 1

    for i in clothes :
        try :
            hashtable[i[1]] += 1
        except:
            hashtable[i[1]] = 1
    
    for key, value in hashtable.items(): # 경우의 수 구하기
        answer *= value+1
        
    return answer-1