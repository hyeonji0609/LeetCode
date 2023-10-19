# LeetCode

Coding test study solving 2 or 3 per week

# git push rule
1. git commit시
  - [작성자명] 문제이름
  - [Hyeonji Jeong] 1768. Merge Strings Alternately
3. 내용
  - python 파일 1개 + 주석으로 시간, 성능 달아놓을 것 !
  - 문제에 대한 해설 1개 (노션 링크 첨부)
  - 예시

```
    import itertools

    class Solution:
      def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        return res.join([x for x in itertools.chain.from_iterable(itertools.zip_longest(list(word1),list(word2))) if x])

    """
    Runtime 35 ms
    Memory 16.1 MB
    """

```
