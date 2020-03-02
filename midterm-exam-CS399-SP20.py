#!/usr/bin/env python
# coding: utf-8

# In[3]:


# you are given 2 files
# one is called auto-train.txt
# the other is called auto-test.txt

_auto_test = open("auto-test.txt")
from textblob import TextBlob
import networkx as nx


# In[4]:


# read the train file one line at a time
# using TextBlob: extract the noun phrases of length-2
_auto_train = open("auto-train.txt")
_list_of_train_nouns = []
for line in _auto_train:
    text = TextBlob(line)
    for noun in text.noun_phrases:
        _list_of_train_nouns.append(noun)


# In[13]:


# using the pairs of noun-phrases produced from above
_list_of_train_pairs = []
for phrase in _list_of_train_nouns:
    comps = phrase.split()
    if len(comps) == 2:
        _list_of_train_pairs.append((comps[0],comps[1]))
        
# construct a network called auto_train_g
auto_train_g = nx.Graph()
auto_train_g.add_edges_from(_list_of_train_pairs)
nx.draw(auto_train_g, with_labels = True)


# In[23]:


# using the auto-test.txt file
# read one line at a time   


# In[10]:


# using TextBlob construct the noun phrases of length-2 for each line a lone
# store the noun phrases resulted from the line in a list


# In[25]:


# add the noun phrases to the auto_train_g network one pair at a time
# count the number of edges in the network before you add each pair and after 


# In[ ]:


# if the number of edges change print the pair that changed the network edges
# also print how many edges were added as you add the pairs


# In[3]:


# when you are done processing the line (with the corresponding noun phrase pairs): 
#          print POSITIVE if the number of edges changed 
#          print NEGATIVE if the number of edges do not change


# In[8]:


# Do that for each line in the auto-test.txt


# In[14]:


_auto_test = open("auto-test.txt")
_auto_test_noun_list = []
for line in _auto_test:
    _auto_test_noun_list = []
    text = TextBlob(line)
    for noun in text.noun_phrases:
        _auto_test_noun_list.append(noun)
    _auto_test_pair_noun_list = []
    for phrase in _auto_test_noun_list:
        comps = phrase.split()
        if len(comps) == 2:
            _auto_test_pair_noun_list.append((comps[0],comps[1]))
    for pair in _auto_test_pair_noun_list:
        previous_num_of_edges = int(auto_train_g.number_of_edges())
        auto_train_g.add_edge(pair[0],pair[1])
        num_of_edges = int(auto_train_g.number_of_edges())
        if num_of_edges > previous_num_of_edges:
            print("#########","\nFor line: '", line, "'")
            print("This pair: (",pair[0],",",pair[1],") changed the number of edges:")
            print("The graph has",auto_train_g.number_of_edges(),"Edges")
            print("The number of edges increased by: ",num_of_edges - previous_num_of_edges)
            print("Change in number of edges:","POSITIVE")
        else:
            print("########","\nFor line: '", line, "'")
            print("Change in number of edges:","NEGATIVE")


# In[1]:





# In[ ]:


#professor this is the original line of codes I wrote before talking to you about this portion of the project in class.
#The top part is the correct code.
#_auto_test = open("auto-test.txt")
#_auto_test_noun_list = []
#for line in _auto_test:
#    text = TextBlob(line)
#    for noun in text.noun_phrases:
#        _auto_test_noun_list.append(noun)
        
#_auto_test_pair_noun_list = []
#for phrase in _auto_test_noun_list:
#    comps = phrase.split()
#    if len(comps) == 2:
#        _auto_test_pair_noun_list.append((comps[0],comps[1]))
        
#print("The graph has",auto_train_g.number_of_edges(),"Edges")

#for pair in _auto_test_pair_noun_list:
#    previous_num_of_edges = int(auto_train_g.number_of_edges())
#    auto_train_g.add_edge(pair[0],pair[1])
#    num_of_edges = int(auto_train_g.number_of_edges())
#    if num_of_edges > previous_num_of_edges:
#        print("This pair: (",pair[0],",",pair[1],") changed the number of edges:")
#        print("The graph has",auto_train_g.number_of_edges(),"Edges")
#        print("The number of edges increased by: ",num_of_edges - previous_num_of_edges)
#        print("POSITIVE")
#    else:
#        print("NEGATIVE")

