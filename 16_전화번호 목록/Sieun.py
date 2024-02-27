def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1): # 루프가 끝까지 도는 경우, 마지막 i는 비교대상 없음
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
                
    return True