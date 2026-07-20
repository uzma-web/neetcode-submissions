class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=[]
        for i in s:
            if i.isalnum():
                a.append(i.lower())
        i=0
        j=len(a)-1
        mark=0
        while(i<=j):
            if a[i]!=a[j]:
                mark=1
            i+=1
            j-=1
        if mark==0:
            return True
        return False