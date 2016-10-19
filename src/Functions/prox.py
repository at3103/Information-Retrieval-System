import math

def proximity(text,q):
	index = 0
	for w in text:
		if w == q:
			break
		else:
			index+=1

	scores = []

	for i in range(0,len(text)):
		D = abs(i - index)
		if D != 0:
			v = math.log((1+1/D),2)
		else:
			v = 0
		scores.append((text[i],v))	 
	return scores	