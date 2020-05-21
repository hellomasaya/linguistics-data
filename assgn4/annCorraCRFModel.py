#!/usr/bin/env python
# coding: utf-8

# In[44]:


import re
import pickle
from sklearn_crfsuite import CRF
from sklearn_crfsuite import metrics
from sklearn_crfsuite import scorers


# In[45]:


def parse(input_):
    tags = []
    lexicons = []
    lemma = []
    pos= []
    sentences = input_.split("\n\n")
    for sentence in sentences:
        words = sentence.split("\n")
        for word in words:
            tokens = word.split("\t")
            tags.append(tokens[7])
            lexicons.append(tokens[1])
            pos.append(tokens[4])
            lemma.append(tokens[2])
        lexicons.append("</s>")
        tags.append("</s>")
        lemma.append("</s>")
        pos.append("</s>")
    
    lexicons.pop()
    return lexicons, tags, pos, lemma


# In[46]:


def features(sentence, index, pos_sentence):
#     print(sentence[index], pos_sentence[index])
    ### sentence is of the form [w1,w2,w3,..], index is the position of the word in the sentence
    return {
        'word':sentence[index],
        'is_first_word': int(index==0),
        'is_last_word':int(index==len(sentence)-1),
        'prev_word':'' if index==0 else sentence[index-1],
        'next_word':'' if index==len(sentence)-1 else sentence[index+1],
        'prev_pre_word':'' if index==0 or index==1 else sentence[index-2],
        'next_next_word':'' if index==len(sentence)-1 or index==len(sentence)-2 else sentence[index+2],
        'is_numeric':int(sentence[index].isdigit()),
        'is_alphanumeric': int(bool((re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])',sentence[index])))),
        'pos': pos_sentence[index]
         }


# In[47]:


def prepareData(input):
    lexicons, tags, pos, lemma = parse(input)
#     print(len(lexicons))
    sentences = ' '.join(lexicons).split(' </s> ')
    sentences_pos = ' '.join(pos).split(' </s> ')
    sentences_tags = ' '.join(tags).split(' </s> ')
#     print(len(sentences))
    X=[]
    y=[]
    for sentenceid, sentence in enumerate(sentences):
        words = sentence.split(' ')
        pos = sentences_pos[sentenceid].split(' ')
        X.append([features(words, index, pos) for index in range(len(words))])
    for sentence_tag in sentences_tags:
        words_tag = sentence.split(' ')
        y.append(words_tag)
    return X, y


# POS, Chunck, Lemma, Case Marking

# In[48]:


def train_CRF(X_train,y_train):   
    crf = CRF(
        algorithm='lbfgs',
        c1=0.01,
        c2=0.1,
        max_iterations=100,
        all_possible_transitions=True
    )
    crf.fit(X_train, y_train)
    pickle.dump(crf, open("./annCorra_crf_pos_model", 'wb'))


# In[49]:


# print(X_train[0])
# print(y_train)


# In[50]:


def test_dev_data(X_test,y_test):
    y_pred=crf.predict(X_test)
    print("F1 score on Test Data ")
    print(metrics.flat_f1_score(y_test, y_pred,average='weighted',labels=crf.classes_))
    print("F score on Training Data ")
    y_pred_train=crf.predict(X_train)
    metrics.flat_f1_score(y_train, y_pred_train,average='weighted',labels=crf.classes_)

    ### Look at class wise score
    print(metrics.flat_classification_report(
        y_test, y_pred, labels=crf.classes_, digits=3
    ))


# In[51]:


train_file = open('./final_train.txt', 'r', encoding="utf-8")
traininput = train_file.read()

# dev_file = open('./final_dev.txt', 'r', encoding="utf-8")
# devinput = dev_file.read()


# In[52]:


X_train,y_train = prepareData(traininput)


# In[53]:


train_CRF(X_train, y_train)


# In[54]:


# X_test,y_test = prepareData(devinput)


# In[32]:


# test_dev_data(X_test, y_test)


# In[ ]:





# In[ ]:




