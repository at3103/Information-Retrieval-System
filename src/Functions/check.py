import sys
from .. classes.query import *
from global_const import *	
from .. classes.documents import Document
from .. classes.documents import Rel_doc
from .. classes.word_set import Word_set
from .display_output import *

def check_precision():
	if float(Query.precision) <= 0.0:
		Final(None, Query.search_term,Query.precision)

def check_number_results(number):
	if number <10:
		print ("Exiting!!!!")
		return

def check_relevance_count():
	if Rel_doc.count == 0:
		print ("Sorry, no relevant results found!!")
		return 0
	# Break if number of relevant documents is 10 OR if current precision >= desired precision
	if Rel_doc.count == n or Rel_doc.count/n >= float(Query.precision):
		display(2, None, Query.search_term, Rel_doc.count/n)
		return 0
	return 1