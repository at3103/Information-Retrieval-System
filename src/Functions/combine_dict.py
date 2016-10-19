from collections import Counter

def combine_dict(d1, d2, doc_flag = None):
	
	'''Compute Document Frequency'''
	if doc_flag == 1:
		return dict(Counter(list(d1.keys())+ list(d2.keys())))

	else:
		temp ={}
		temp.update(d1)
		temp.update(d2)

		for x in d1.keys():
			temp[x] = d1[x] + d2.get(x,0)
		return temp
