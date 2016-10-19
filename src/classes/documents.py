
from .word_set import Word_set
from .. Functions.combine_dict import combine_dict


class Document(object):

	total = 0
	relevance_count = 0

	"""docstring for Document"""
	def __init__(self, words_dict, relevance = None, flag_first = None):
		super(Document, self).__init__()
		self.relevance = relevance if relevance else 0
		Document.total += 1
		Document.relevance_count +=  1 if relevance else 0
		self.wset = Word_set(words_dict, 1, flag_first)


class Rel_doc(object):
	count = 0
	dictionary = dict()
	word = Word_set(dictionary, 0)
	"""docstring for Rel_doc"""
	def __init__(self, words_dict, flag_first = None):
		super(Rel_doc, self).__init__()
		self.words_dict = words_dict
		Rel_doc.count += 1
		Rel_doc.word.dictionary = combine_dict(Rel_doc.word.dictionary, words_dict)		


class Non_rel_doc(object):
	count = 0
	dictionary = dict()
	word = Word_set(dictionary, 0)

	"""docstring for Non_rel_doc"""
	def __init__(self, words_dict, flag_first = None):
		super(Non_rel_doc, self).__init__()
		self.words_dict = words_dict
		Non_rel_doc.count += 1
		Non_rel_doc.word.dictionary = combine_dict(Non_rel_doc.word.dictionary, words_dict)