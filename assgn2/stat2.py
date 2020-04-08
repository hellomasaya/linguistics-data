from collections import defaultdict
import json 

f1 = open('20171099_a2.txt','r')

stat = defaultdict(int)
stat2 = defaultdict(int)

sentences = f1.read().split('----------------------------------------\n')
for sentence in sentences:
    lines = sentence.split('\n')
    lines.pop()
    print(lines)
    for i in range(len(lines)):
        if(lines[i][0]=='<' or lines[i][0]=='\n'):
            continue
        tags=lines[i].split('\t')
        print(tags[1],tags[5])
        stat[tags[5]]+=1
        if(tags[5]=='lwg__psp'):
            if(lines[int(tags[5])][0]=='<' or lines[int(tags[5])][0]=='\n'):
                continue
            tag_prev = lines[int(tags[5])].split('\t')
            stat2[tags[1]+","+tag_prev[5]]+=1
f1.close()

sorted_stat = {k: v for k, v in sorted(stat.items(), key=lambda item: item[1], reverse=True)}
sorted_stat2 = {k: v for k, v in sorted(stat2.items(), key=lambda item: item[1], reverse=True)}
f2 = open('stat.txt', 'w')
f2.write('Tag frequency\n---\n')
for key in sorted_stat:
    f2.write(key+":"+str(sorted_stat[key])+"\n")
f2.write('---\nTag frequency with case markers\n---\n')
for key in sorted_stat2:
    f2.write(key+":"+str(sorted_stat2[key])+"\n")
f2.close()

# f2.write()