import sys
from .. classes.query import *
from nltk.corpus import words
from global_const import *	

original_q = sys.argv[1]

def Initial(augment, modified_q,curr_precision):
	print ("Total no of results : ", n)
	print ("Bing Search Results:")
	return

def Second(augment, modified_q,curr_precision):
	print ("Current Precision   = ", curr_precision)
	print ("Augmenting With     = ", augment)
	print ("Modified Query = ", modified_q)
	Initial(None, None, None)
	return

def Final(augment, modified_q ,curr_precision):
	print ("Final Precision =", curr_precision)
	print ("Final Query =", modified_q)
	print ("Desired precision reached!!")
	sys.exit()
	
switch = { 0 : Initial,
		   1 : Second,
		   2 : Final
}

def display(flag, augment = None, modified_q = None, curr_precision = None):
	print ("\nParameters:")
	print ("Original Query      = ", original_q)
	print ("Desired Precision   = ", Query.precision)
	switch[flag](augment, modified_q, curr_precision)
	return 
