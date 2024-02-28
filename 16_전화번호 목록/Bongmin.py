def solution(phone_book):
    phone_book.sort()  # 전화번호를 오름차순 정렬
    
    for i in range(len(phone_book) - 1):
        # 다음 전화번호가 이번 전화번호로 시작하는지를 검사하는 startswith 
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
            
    return True