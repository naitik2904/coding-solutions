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
	    
