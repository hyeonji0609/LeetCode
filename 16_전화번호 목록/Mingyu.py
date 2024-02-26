# 리스트 풀이
def solution(phone_book):
    # phone_book을 오름차순 정렬
    sorted_book = sorted(phone_book)
    # i를 전체 리스트 하나 전까지만 순회(마지막은 비교 대상이 없음)
    for i in range(len(sorted_book)-1):
        # i의 다음 인덱스가 i로 시작하면 return False
        if sorted_book[i+1].startswith(sorted_book[i]):
            return False
    # 전체 순회 후 없으면 return True
    return True

# Hashmap 풀이
def solution(phone_book):
    phone_map = {}  # 해시맵 초기화
    # 정렬된 phone_book의 각 요소 순회
    for phone_number in sorted(phone_book):
        temp = "" # 빈 문자열 초기화
        # 각 요소(문자열) 순회
        for number in phone_number:
            # 빈 문자열에 요소(문자열) 내의 각 문자 할당
            temp += number
            if temp in phone_map:  # 현재 전화번호가 해시맵에 이미 존재하는지 확인
                return False
        phone_map[phone_number] = 1  # 현재 전화번호를 해시맵에 추가
    return True