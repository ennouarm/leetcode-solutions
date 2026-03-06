from collections import defaultdict

def longest_w_r_c(s:str)->int:
    longest = 0
    l=0
    counter : dict[str, int] = defaultdict(int)
    for r in range(len(s)):
        counter[s[r]]+=1
        while counter[s[r]]>1:
            counter[s[l]]-=1
            l+=1
        longest = max(longest,r-l+1)
    return longest
if __name__=="__main__":
    s = "aaaabaaa"
    res = longest_w_r_c(s)
    print(res)