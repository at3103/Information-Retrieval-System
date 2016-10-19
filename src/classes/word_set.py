from .. Functions.combine_dict import combine_dict

'''Create Word_set for each document'''
class Word_set(object):
	"""docstring for Word_set"""
	total = 0
	dict_wrd_freq = dict()
	dict_doc_freq = dict()
	def __init__(self, words_dict, doc_subclass_flag,flag_first = None):
		super(Word_set, self).__init__()
		self.words_count = len(words_dict)
		self.dictionary = words_dict
		self.dict_wrd_freq = dict()
		self.weights = dict()
		Word_set.prox = dict()
		if doc_subclass_flag == 1:
			Word_set.dict_wrd_freq = combine_dict(Word_set.dict_wrd_freq,self.dictionary)
			Word_set.dict_doc_freq = combine_dict(Word_set.dict_doc_freq,self.dictionary, 1)
			Word_set.total += len(Word_set.dict_wrd_freq) 


	def make_set(self):
		combine_dict(Word_set.dict_wrd_freq, dictionary)
		combine_dict(Word_set.dict_doc_freq,dictionary, 1)
		Word_set.total += len(Word_set.dict_wrd_freq) 
	
	def update_set(self):
		self.dict_wrd_freq = dict.fromkeys(Word_set.dict_wrd_freq, 0)
		self.dict_wrd_freq.update(self.dictionary)
		self.weights = dict.fromkeys(Word_set.dict_wrd_freq, 0)
		Word_set.prox = dict.fromkeys(Word_set.dict_wrd_freq, 0)
