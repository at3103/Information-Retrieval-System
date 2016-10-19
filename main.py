#from py_bing_search import PyBingWebSearch
from key import bing
from urllib.request import *
from urllib.parse import *
import base64
import sys
from collections import Counter
import json
import math
from pprint import pprint
import operator
import nltk
from nltk.corpus import stopwords
from nltk.corpus import words
from global_const import *	
from src.classes.documents import Document
from src.classes.documents import Rel_doc
from src.classes.documents import Non_rel_doc
from src.classes.word_set import Word_set
from src.classes.query import Query
from src.Functions.display_output import *
from src.Functions.prox import *
from src.Functions.check import *
from src.algorithms.algorithm1 import *

original_q = sys.argv[1]

def stopWordElimination(all_words):
	stop_words = [line.rstrip('\n') for line in open('stop_words.txt')]
	stop_words += stopwords.words('english')
	w = [word for word in all_words if word not in stop_words if word.isalpha()]
	return w

def split(string):
	all_words = nltk.word_tokenize(string)
	aft_elimination = stopWordElimination(all_words)
	return aft_elimination

def bing_search(search_term, precision):
	q_prev = {}
	
	#Initial Display details
	display(0)
	
	# Break if desired precision is less than equal to 0.0
	check_precision()


	while True:
		words=[]
		result = []
		docs =[]
		rel_docs = []
		non_rel_docs = []

		title = []
		desc = []
		scores_all = []

		Document.count = 0
		Document.relevance_count = 0
		Rel_doc.count = 0
		Non_rel_doc.count = 0
		'''
		url='http://api.datamarket.azure.com/Bing/Search/Web?Query=%27'+search_term+'%27&$top=10&$format=Atom'
		headers = {'Authorization': 'Basic ' + bing}
		#r = requests.get(url, headers=headers)
		r = urllib.request(url,headers=headers)
		js = r.urlopen(r).read()
		info = json.loads(js.decode("utf-8"))
		#data = r.json()
		#x=data.get('d').get('results')
		print(info)
		'''
		# Bing search with search term



		bingUrl = 'https://api.datamarket.azure.com/Bing/Search/Web?Query=%27'+quote(search_term)+'%27&$top=10&$format=json'


		print("URL: ", bingUrl)
		#Provide your account key here
		accountKey = bing

		accountKeyEnc = base64.b64encode(bytes((accountKey + ':' + accountKey), 'UTF-8'))
		headers = {'Authorization': 'Basic ' + accountKeyEnc.decode('utf-8')}
		req = Request(bingUrl, headers = headers)
		response = urlopen(req)
		content = response.read().decode('utf-8')
		result = json.loads(content)['d']['results']
		#content contains the xml/json response from Bing. 




        #url ='https://api.datamarket.azure.com/Bing/Search/Web?Query=%27' + search_term + '%27&$top=10&$format=Atom'
    	#url ="https://api.datamarket.azure.com/Bing/Search/Web?Query=%27" + search_term + "%27&$top=10&$format=Atom"
    	

		#bing_web = PyBingWebSearch(bing, search_term, web_only=False)
		#result = bing_web.search(limit=n, format='json') #1-n


		'''
		bingUrl = 'https://api.datamarket.azure.com/Bing/Search/Web?Query=%27'+search_term+'%27&$top=10&$format=json'
		#Provide your account key here
		accountKey = bing

		accountKeyEnc = base64.b64encode(accountKey + ':' + accountKey)
		headers = {'Authorization': 'Basic ' + accountKeyEnc}
		req = urllib2.Request(bingUrl, headers = headers)
		response = urllib2.urlopen(req)
		data = response.read()
		r = json.loads(data)
		#content contains the xml/json response from Bing. 
		result = r['d']['results']#data.get('d').get('results')
		print(result)
		'''

		
		# Exception: If number of search results returned is less than 10
		if(check_number_results(len(result)) == 0):
			return
		
		for x in range(0,n):
			print ("\n Result :", (x+1))
			print ("\nTitle: " + result[x]['Title'])	
			print ("URL: " +result[x]['Url'])
			print ("Summary: " +result[x]['Description'])
			
			# User Input
			relevant = input("Relevant (Y/N)?")
						
			# Tokenize the words
			q = nltk.word_tokenize(search_term)[0]
			title = split(str(result[x]['Title'].lower()))
			desc  = split(str(result[x]['Description'].lower()))
			scores_all.append(proximity(title,q))
			scores_all.append(proximity(desc,q)) 
			
			tokens = split(str(result[x]['Title'].lower()) + " " + str(result[x]['Description'].lower())) #+ " " + result[x]['Url'].lower())
			words = dict(Counter(tokens))
			
			if relevant == 'Y' or relevant == 'y':
				docs.append(Document(words,1))
				rel_docs.append(Rel_doc(words))
			else:
				docs.append(Document(words,0))
				non_rel_docs.append(Non_rel_doc(words))
		
		#Number of relevant documents
		relevance_count = Rel_doc.count

		#Exit based on relevance
		if(check_relevance_count() == 0):
			return 0
		
		finalset = list(Word_set.dict_wrd_freq.keys())

		for d in docs:
			d.wset.update_set()
			for w in Word_set.dict_wrd_freq.keys():
				d.wset.weights[w] =  d.wset.dict_wrd_freq[w] * math.log(n/Word_set.dict_doc_freq[w]) 

		finalset_curr=finalset

		#Proximity Finalization
		for w in Word_set.dict_wrd_freq.keys():
			sc = 0
			for i in range(0,len(scores_all)):
				for j in range(0,len(scores_all[i])):
					if scores_all[i][j][0] == w:
						sc += scores_all[i][j][1]

			Word_set.prox[w]=sc		


		# # ROCCHIO's CALL
		q_prev,q_curr = rocchio(q_prev,docs)

		sorted_q_curr = sorted(q_curr.items(), key=operator.itemgetter(1), reverse=True)


		top_ten ={}

		for j in range(0,10):
			w = sorted_q_curr[j][0] 
			top_ten[w] = Word_set.prox[w]		

		top_ten_prox_dict = sorted(top_ten.items(), key=operator.itemgetter(1), reverse = True)


		# Appending new terms to search term
		
		count_terms = 0
		augment = ""
		for i in range(0,len(top_ten_prox_dict)):
			q = top_ten_prox_dict[i][0]
			if q not in search_term:
			#if q not in search_term: #and q not in validwords:
				augment += " " + q
				search_term += " " + q
				count_terms+=1
			if count_terms==2:
				break	
		
		Query.search_term = search_term
		search_term_token = split(search_term)
		q_prev = q_curr	

		display(1, augment, search_term, relevance_count/n)

	display(2, None, search_term, relevance_count/n)
bing_search(sys.argv[1], sys.argv[2])
