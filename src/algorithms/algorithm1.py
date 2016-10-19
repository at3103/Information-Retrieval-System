from src.classes.documents import Document
from src.classes.documents import Rel_doc
from src.classes.documents import Non_rel_doc
from src.classes.word_set import Word_set
from src.classes.query import Query
from global_const import *	

from src.Functions.display_output import *
from src.Functions.check import *

# ROCCHIO's ALGORITHM
def rocchio(q_prev, docs):		
	sum_relevance= {}
	sum_not_relevance = {}
	q_curr = {}
	temp ={}
		
	sum_relevance= dict.fromkeys(Word_set.dict_wrd_freq, 0)
	sum_not_relevance = dict.fromkeys(Word_set.dict_wrd_freq, 0)
	q_curr = dict.fromkeys(Word_set.dict_wrd_freq, 0)

	temp = q_prev
	q_prev = dict.fromkeys(Word_set.dict_wrd_freq, 0)
	q_prev.update(temp)


	for j in Word_set.dict_wrd_freq.keys():
		for d in docs:
			if d.relevance == 1:
				sum_relevance[j] += d.wset.weights[j]
			else:
				sum_not_relevance[j]  += d.wset.weights[j]	


	# Calculating scores for modified query vector
	for j in Word_set.dict_wrd_freq.keys():
		q_curr[j] = q_prev[j] * alpha + beta * (sum_relevance[j]/Rel_doc.count) - gamma * (sum_not_relevance[j]/(n - Rel_doc.count))

	return q_prev, q_curr