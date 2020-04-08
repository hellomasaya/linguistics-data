from collections import defaultdict
import json 

f1 = open('20171099_a2.txt','r')

stat = defaultdict(int)

sentences = f1.read()
sentence = sentences.split('\n')
for line in sentence:
    # print(line)
    if(line[0]=='<' or line[0]=='-' or line[0]=='\n'):
        continue
    tags=line.split('\t')
    # print(tags[1],tags[6])
    stat[tags[6]]+=1
f1.close()

print(stat)
sorted_stat = {k: v for k, v in sorted(stat.items(), key=lambda item: item[1], reverse=True)}
print(sorted_stat)
f2 = open('stat.txt', 'w')
for key in sorted_stat:
    f2.write(key+":"+str(sorted_stat[key])+"\n")
f2.close()
# f2.write()