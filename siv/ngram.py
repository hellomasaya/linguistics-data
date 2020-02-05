import sys
import os
import operator
import itertools  

f = open('./20171099_asgn1.txt', 'r')

result=[]
for x in f.readlines():
    result.append(x.split('\t')[2])
f.close()

dict_bigrams = {}

for i in range(len(result)-1):
    if (result[i], result[i+1]) in dict_bigrams:
        dict_bigrams[(result[i], result[i+1])] += 1
    else:
        dict_bigrams[(result[i], result[i+1])] = 1

sorted_x = sorted(dict_bigrams.items(), key=operator.itemgetter(1))[::-1]
print("----------------2 gram POS----------------")
for i in range(20):
    print(sorted_x[i])

print("\n\n\n")

f = open('./20171099_asgn1.txt', 'r')

result_dep=[]
for x in f.readlines():
    result_dep.append(x.split('\t')[9].strip("\n"))
f.close()
###############################################################################

f = open('./20171099_asgn1.txt', 'r')

result=[]
for x in f.readlines():
    result.append(x.split('\t')[2])
f.close()

dict_bigrams = {}

for i in range(len(result)-2):
    if (result[i], result[i+1], result[i+2]) in dict_bigrams:
        dict_bigrams[(result[i], result[i+1], result[i+2])] += 1
    else:
        dict_bigrams[(result[i], result[i+1], result[i+2])] = 1

sorted_x = sorted(dict_bigrams.items(), key=operator.itemgetter(1))[::-1]
print("----------------3 gram POS----------------")
for i in range(20):
    print(sorted_x[i])

print("\n\n\n")
###############################################################################


f = open('./20171099_asgn1.txt', 'r')

result_dep=[]
for x in f.readlines():
    result_dep.append(x.split('\t')[9].strip("\n"))
f.close()

# print(result_dep)

dict_bigrams_dep = {}

for i in range(len(result_dep)-1):
    if (result_dep[i], result_dep[i+1]) in dict_bigrams_dep:
        dict_bigrams_dep[(result_dep[i], result_dep[i+1])] += 1
    else:
        dict_bigrams_dep[(result_dep[i], result_dep[i+1])] = 1

sorted_y = sorted(dict_bigrams_dep.items(), key=operator.itemgetter(1))[::-1]
print("----------------2 gram DEP----------------")
for i in range(20):
    print(sorted_y[i])
print("\n\n\n")

###############################################################################


f = open('/home/priyank/Downloads/20171095_asgn1.txt', 'r')

result_dep=[]
for x in f.readlines():
    result_dep.append(x.split('\t')[9].strip("\n"))
f.close()

# print(result_dep)

dict_bigrams_dep = {}

for i in range(len(result_dep)-2):
    if (result_dep[i], result_dep[i+1], result_dep[i+2]) in dict_bigrams_dep:
        dict_bigrams_dep[(result_dep[i], result_dep[i+1], result_dep[i+2])] += 1
    else:
        dict_bigrams_dep[(result_dep[i], result_dep[i+1], result_dep[i+2])] = 1

sorted_y = sorted(dict_bigrams_dep.items(), key=operator.itemgetter(1))[::-1]
print("----------------3 gram DEP----------------")
for i in range(20):
    print(sorted_y[i])
###############################################################################
