# Information-Retrieval-System
 
        Ashwin Tamilselvan - at3103                                                 Niharika Purbey - np2544 


Bing Account Key:

The key needs to be added to the file key.py 

To run:
python3 main.py '<search_term>' <precision>
(Python 3)

Example: python3 main.py 'musk' 0.9

Internal Design:
main.py: 
The main driver program. It takes care of user input/interaction, getting results from the search engine, modifying the query for further iterations, calculating precision and deciding when to break from the program.
global_const.py:
Contains values of all the constant variables
key.py:
Contains the bing key
stop_words.txt:
Contains a list of stop words

Within src:
1) algorithms 
algorithm1.py:
Contains the main algorithm for Relevance Feedback. Rocchio's algorithm - explained later 
2) classes [These are helper classes]
documents.py: Information about relevant and non-relevant documents 
query.py: For precision
word_set.py: Initializing and setting the term frequency and document frequency 
3) Functions
check.py: Checks to make decisions like when to break.
combine_dict.py: Method to computer document frequency
display_output.py: Contains all the relevant print statements
prox.py: Calculates the proximity of words


Relevance Feedback Algorithm:

To generate new search terms, we used the title and the description of the relevant search results. We split the words using NLTK's word tokenizer and then got rid of the stop words. We calculated the weight of each word using the following formula: 
Wi,j = tfi,j * log(N/dfi)

where tfi,j is the number of times the term i has occured in document j
N is the total number of documents
dfi is the number of docuents where term i has occured.

We the used ROCCHIO's Algorithm to provide relevance feedback [1]:
qm = α*q0 + β1/|Dr|* ∑ dj(dj∈Dr) + γ/|Dnr| * ∑ dj(dj∈Dnr)

After trying many combinations of constants, we found the following values to be good parameters for Rocchio's algorithm. 
alpha = 1
beta  = 0.75
gamma = 0.15

In addition to this, we also used term proximity in the calculation of relevance feedback[2]. 
We used the follwoing formula:
df(x,y) = log(1+1/D(x,y)) where df(x,y) : logarithmic based distance factor between terms x,y 
where x is query term and y is probable query expansion term. 
D(x,y) : distance between x and y among relevant docs

If a term is closer to the orginial search term, it would be more relevant and should have a higher chance of occuring in the new query term. We added the proximity value to ROCCHIO's algorithm, to give such words a higher score.

So we selected the top ten results generated from Rocchio's algorithm, and from the top ten we selected those 2 terms which had the highest proximity value. 


References:
[1] C. Manning, P. Raghavan and H. Schütze, "Introduction to Information Retrieval", Cambridge University Press. 2008
[2] O. Vechtomova and Y. Wang, “A Study of the Effect of Term Proximity on Query Expansion,” Inf. Sci., pp. 1–19, 2006

