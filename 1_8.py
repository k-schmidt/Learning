'''
Python allows negative integers to be used as indices into a sequence, 
such as a string. If string s has length n, and expression s[k] is used for in- 
dex -n<=k<0, what is the equivalent index j>=0such that s[j] references 
the same element?
'''

def index_locate(data, k):
	idx = k - len(data)
	if data:
		print data[idx], idx
		return data[idx], idx
	else:
		False

if __name__ == '__main__':
	index_locate([1,2,3,4,5], 4)
	index_locate([1,2,3,4,5], 2)        
