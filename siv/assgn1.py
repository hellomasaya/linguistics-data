#!/usr/bin/env python
# coding: utf-8

# In[20]:


import stanfordnlp
nlp = stanfordnlp.Pipeline(lang='hi')
# Download hindi models: https://stanfordnlp.github.io/stanfordnlp/models.html#human-languages-supported-by-stanfordnlp
# on the model_path = ~/stanfordnlp_resources/


# In[23]:


def dependencies():
    corpus = open('./corpus_1055.txt', 'r')
    corpus = corpus.read()
    sentences = corpus.split('\n')
    for sentence in sentences:
        print("<s>")
        doc = nlp(sentence)
        doc.sentences[0].print_dependencies()


# In[25]:


# run on terminal to get the output: python3 assgn1.py > dependency_asgn1.txt
## where assign1.py has **this cell and the above ones only**
dependencies()


# In[27]:


# def preprocess():
#     file = open('dependency_asgn1.txt', 'r')
#     file = file.read()
#     sentences = file.split("<s>")
#     for sentence in sentences:
#         print(sentence)


# In[28]:


# preprocess()


# In[ ]:




