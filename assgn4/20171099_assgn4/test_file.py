#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pickle
import sys
import re
from sklearn_crfsuite import metrics

def make_output_file(pred):
#    print(pred)
    file = open('20171099_output.txt', 'w+')
    file1 = open('test_data_words.txt', 'r').read()
    sentences = file1.split(' </s> ')
    for i,sentence in enumerate(sentences):
        words = sentence.split(' ')
        lent = len(words)
        for j in range(lent):
            file.write(words[j])
            file.write("\t")
            file.write(pred[i][j])
            file.write("\n")
    file.close()


# In[41]:


def test_dev_data(X_test,y_test, model):
#     model = './annCorra_crf_all_features_model'
    crf = pickle.load(open(model, 'rb'))
    
    y_pred=crf.predict(X_test)
    
    print("Accuracy: ", metrics.flat_accuracy_score(y_test, y_pred))
    print("F1 score on Test Data: ", metrics.flat_f1_score(y_test, y_pred,average='weighted',labels=crf.classes_))
    print("Precision score on Test Data: ", metrics.flat_precision_score(y_test, y_pred,average='weighted',labels=crf.classes_))
    print("Recall score on Test Data: ", metrics.flat_recall_score(y_test, y_pred,average='weighted',labels=crf.classes_))
    print("Class Wise Score")
    print(metrics.flat_classification_report(y_test, y_pred, labels=crf.classes_, digits=3))
    
    return y_pred


# In[28]:


def parse(input_):
    tags = []
    lexicons = []
    lemma = []
    pos = []
    tam = []
    gender = []
    number = []
    person = []
    sentences = input_.split("\n\n")
    for sentence in sentences:
        words = sentence.split("\n")
        for word in words:
            tokens = word.split("\t")
            try:
                tags.append(tokens[7])
                lexicons.append(tokens[1])
                pos.append(tokens[4])
                lemma.append(tokens[2])
                extra = tokens[5].split("|")
                for info in extra:
                    if "tam" in info:
                        tam_ = info.split("-")
                        tam.append(tam_[1])
                    if "gen" in info:
                        gen_ = info.split("-")
                        gender.append(gen_[1])
                    if "num" in info:
                        num_ = info.split("-")
                        number.append(num_[1])
                    if "pers" in info:
                        pers_ = info.split("-")
                        person.append(pers_[1])
            except:
                print(sentence)  
        lexicons.append("</s>")
        tags.append("</s>")
        lemma.append("</s>")
        pos.append("</s>")
        tam.append("</s>")
        gender.append("</s>")
        number.append("</s>")
        person.append("</s>")
    
    lexicons.pop()
    tags.pop()
    lemma.pop()
    pos.pop()
    tam.pop()
    gender.pop()
    number.pop()
    person.pop()
    file = open('test_data_words.txt', 'w+')
    file.write(' '.join(lexicons))
    file.close()
    return lexicons, tags, pos, lemma, tam, gender, number, person


# In[14]:


def features(sentence, index, pos_sentence, tam, g, n ,p, lemma):
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
        'pos': pos_sentence[index],
        'tam':tam[index],
        'gender': g[index],
        'number':n[index],
        'person':p[index],
        'lemma': lemma[index]
         }


# In[15]:


def prepareData(input):
    lexicons, tags, pos, lemma, tam, g, n ,p = parse(input)
#     print(len(lexicons))
    sentences = ' '.join(lexicons).split(' </s> ')
    sentences_pos = ' '.join(pos).split(' </s> ')
    sentences_tags = ' '.join(tags).split(' </s> ')
    sentences_tam = ' '.join(tam).split(' </s> ')
    sentences_g = ' '.join(g).split(' </s> ')
    sentences_n = ' '.join(n).split(' </s> ')
    sentences_p = ' '.join(p).split(' </s> ')
    sentences_lemma = ' '.join(lemma).split(' </s> ')
#     print(sentences_tags)
#     print(len(sentences))
    X=[]
    y=[]
    for sentenceid, sentence in enumerate(sentences):
        words = sentence.split(' ')
        pos = sentences_pos[sentenceid].split(' ')
        tam = sentences_tam[sentenceid].split(' ')
        g = sentences_g[sentenceid].split(' ')
        n = sentences_n[sentenceid].split(' ')
        p = sentences_p[sentenceid].split(' ')
        lemma = sentences_lemma[sentenceid].split(' ')
        X.append([features(words, index, pos, tam, g, n ,p, lemma) for index in range(len(words))])
    for sentence_tag in sentences_tags:
        words_tag = sentence_tag.split(' ')
        y.append(words_tag)
    return X, y


# In[45]:

test_corpus = sys.argv[2]
test_file = open(test_corpus, 'r', encoding="utf-8")
testinput = test_file.read()
model = sys.argv[1]


# In[29]:


X_test,y_test = prepareData(testinput)


# In[42]:


predicted_labels = test_dev_data(X_test, y_test, model)


# In[40]:


make_output_file(predicted_labels)


# In[39]:
