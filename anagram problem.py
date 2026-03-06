#anagram problem
# for example for ["eat","tea","aet", "tan","ant", ""tna","bat", "tab"]

from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)
    
    for s in strs:
        key = "".join(sorted(s))
        anagram_map[key].append(s)
    return list(anagram_map.values())

print(group_anagrams(["eat","tea","aet", "tan","ant", "tna","bat", "tab"]))