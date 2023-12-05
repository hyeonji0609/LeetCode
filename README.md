# LeetCode

Coding test study solving 2 or 3 per week

# git push rule
1. git commit시
  - 커밋 명 : [커밋 한 사람 이름] 날짜_해결한 문제 번호
    - [Hyeonji Jeong] 20231114_1768,1431
  
2. 업로드 시 폴더 구성
  - 폴더 명 : 주차_문제번호. 문제 명
    - ex) 1_1768. Merge Strings Alternately
  - 문제 설명 파일 명 : 폴더 명과 동일
    - 문제 복붙해서 파일 하나 만들기
  - 파일 명 : 작성자명.py
    - ex) Hyeonji.py

3. 파일 내용
  - python 파일 1개 + 주석으로 설명, 시간, 성능 달아놓을 것 !
  - 문제에 대한 해설 1개 (노션 링크 첨부)
  - 예시

```
    import itertools

    class Solution:
      def mergeAlternately(self, word1: str, word2: str) -> str: 
        res=""
        return res.join([x for x in itertools.chain.from_iterable(itertools. zip_longest(list(word1),list(word2))) if x]) // 설명

    """
    Runtime 35 ms
    Memory 16.1 MB
    """

```
