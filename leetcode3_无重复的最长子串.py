class Solution(object):
    # 字符串中只有26个字母
    def lengthOfLongestSubstring01(self, s):
        """
        :type s: str
        :rtype: int
        """
        map=[0 for i in  range(0,26)] #26字母是否在窗口内出现
        res=0
        left=0
        right=0
        l=len(s)
        while right<l:
            c=s[right]
            map[ord(c)-ord('a')]+=1
            while left<right and map[ord(c)-ord('a')]>1: #左窗口往前挪动
                cl = s[left]
                map[ord(cl) - ord('a')] -= 1
                left+=1
            res=max(res,right-left+1)
            right+=1
        return res

    def lengthOfLongestSubstring(self, s):
        occ=set()
        res=0
        left=0
        right=0
        l=len(s)
        while right<l:
            c=s[right]
            while c in occ: #c 存在于occ中，左窗口需要往前挪动
                occ.remove(s[left])
                left+=1
            occ.add(c)
            res=max(res,right-left+1)
            right+=1
        return res
if __name__ == '__main__':
  Solution().lengthOfLongestSubstring(" a")
