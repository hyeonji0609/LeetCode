# 못푼 문제

def solution(phone_book):
    phone_book_ = sorted(list(map(int,phone_book)))
    
    index = 0

    while len(phone_book_) != index :
        prefix = phone_book_[index]
        str_length = len(str(prefix))
        sliced_number = [int(str(s)[:str_length]) for s in phone_book_[index+1:]]

        if prefix in sliced_number:
            return False
            break

        index += 1
    
    return True

"""
Time limit 및 14번에서 오답
"""