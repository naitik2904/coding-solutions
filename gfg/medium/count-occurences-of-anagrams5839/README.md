# Count Occurences of Anagrams

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a word  **pat**  and a text  **txt**. Return the count of the occurrences of anagrams of the word in the text.

 **Example 1:** 

```
Input: txt = "forxxorfxdofr", pat = "for"
Output: 3
Explanation: for, orf and ofr appears in the txt, hence answer is 3.

```

 **Example 2:** 

```
Input: txt = "aabaabaa", pat = "aaba"
Output: 4
Explanation: aaba is present 4 times in txt.

```

 **Constraints:** 
1 <= |pat| <= |txt| <= 105
Both strings contain lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T08:35:11.978Z  

```py
class Solution:

	def allZero(self, freq):
	    for f in freq:
	        if(f != 0):
	            return False
	    
	    return True
	    
	def search(self,pat, txt):
	    # code here
	    m = len(pat)
	    n = len(txt)
	    
	    if m > n:
            return 0
	    
	    freq = [0] * 26
	    for ch in pat:
	        freq[ord(ch) - ord('a')] += 1
	    
	    i = j = 0
	    count = 0
	    
	    while(j < n):
	        
	        ch = txt[j]
	        freq[ord(ch) - ord('a')] -= 1
	        
	        if(j - i + 1 == m):
	            
	            if(self.allZero(freq)):
	                count += 1
	           
	            prevCh = txt[i]
	            freq[ord(prevCh) - ord('a')] += 1
	            i += 1
	            
	        j += 1
	            
	    return count
	    

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1)