import sys

class Query(object):
	precision = sys.argv[2]
	search_term = ""
	"""docstring for Query"""
	def __init__(self, desired_precision, curr_precision):
		super(Query, self).__init__()
		self.desired_precision = desired_precision
		self.curr_precision = curr_precision