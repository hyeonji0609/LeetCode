def decodeString(s):
    stack = []
    # 각 변수 초기화
    current_str = ""
    current_num = 0

    # 입력 문자열의 각 문자를 순회
    for char in s:
        # isdigit로 숫자 확인
        if char.isdigit():
            # 숫자 단위를 생각해서 저장하기
            current_num = current_num * 10 + int(char)
        # 여는 괄호이면
        elif char == "[":
            # 현재 숫자와 문자열을 스택에 저장
            stack.append((current_num, current_str))
            # 초기화
            current_num, current_str = 0, ""
        # 닫는 괄호이면
        elif char == "]":
            # 스택에서 마지막으로 저장한 숫자와 문자열을 꺼냄
            last_num, last_str = stack.pop()
            # 현재 문자열을 업데이트하기
            current_str = last_str + current_str * last_num
        # 문자가 숫자나 괄호가 아니면 현재 문자열에 추가
        else:
            current_str += char
    return current_str
