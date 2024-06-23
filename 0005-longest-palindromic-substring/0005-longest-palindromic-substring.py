class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_odd, max_even = 0,0
        max_odd_string, max_even_string = "", ""
        for i in range(n):
            #check odd max palindrome string
            j,k=i,i
            while j>=0 and k<n and s[j]==s[k]:
                j-=1
                k+=1
            if (k-j-1)>max_odd:
                max_odd = k-j-1
                max_odd_string = s[j+1:k]
            #check for even palindrome
            j,k=i,i+1
            while j>=0 and k<n and s[j]==s[k]:
                j-=1
                k+=1
            if (k-j-1)>max_even:
                max_even = k-j-1
                max_even_string = s[j+1:k]
        if max_odd > max_even:
            return max_odd_string
        return max_even_string
            