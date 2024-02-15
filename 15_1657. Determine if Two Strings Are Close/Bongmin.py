class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 1. 길이가 안맞거나 단어들의 unique가 안 맞으면 False
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        # 2. 길이도 맞고, unique도 맞다면
        else:
            # 3. 유니크와 개수를 세준다
            ############################
            alpha_dict1 = {}
            alpha_dict2 = {}
            for i in word1:
                if i not in alpha_dict1:
                    alpha_dict1[i] = 1
                else:
                    alpha_dict1[i] +=1        
            for i in word2:
                if i not in alpha_dict2:
                    alpha_dict2[i] = 1
                else:
                    alpha_dict2[i] +=1
            ############################
            # 4. 여기서 알파벳의 개수가 안맞으면 바꿀 수 없으므로 정렬해서 안맞다면 False
            if sorted(list(alpha_dict1.values()))!= sorted(list(alpha_dict2.values())):
                return False
            # 5. 그 외의 경우의 수는 없으므로 True
            else:
                return True
'''
runtime : 190ms : beats 36.00%
memoey : 17.26 : beats : 99.84%
'''