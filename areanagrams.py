#"danger" == "garden" 
# looking for anagrams
#freq1, freq2 
#freq1=freq2 -> anagram
#hash-table (dict)

def are_anagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    freq1= {}
    freq2 = {}
    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    for ch in s2:
        if ch in s2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True