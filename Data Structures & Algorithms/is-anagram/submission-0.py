class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s)
        b=list(t)
        mark=0
        a.sort()
        b.sort()
        if len(a)!=len(b):
            mark=1
        else:
            for i in range(0,len(a)-1+1,1):
                if a[i]!=b[i]:
                    mark=1
        if mark==0:
            return True
        return False
        