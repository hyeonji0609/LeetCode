# 각 숫자를 set하여 unique를 찾아낸다
# 겹치는 숫자가 있을긴데 그거 제외하고 출력한다

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 1. set으로 unique만 뽑아낸다
        nums1 = set(nums1)
        nums2 = set(nums2)
        # 2. 각 answer를 담을 공간과 정답 공간을 마련한다.
        res = []
        ans1 = []
        ans2 = []
        # 3.  각 리스트를 돌려 반대편에 없는 숫자만 담아준다
        for i in nums1:
            if i not in nums2:
                ans1.append(i)
        for i in nums2:
            if i not in nums1:
                ans2.append(i)
        # 4. result에 담아주고 출력해준다.
        res.append(ans1)
        res.append(ans2)
        return res
'''
runtime : 133ms beats 93.17%
memory : 16.98mb beats 86.54
'''
