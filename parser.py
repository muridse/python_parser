import random
import os
import glob
import numpy as np
import fractions

with open('text.txt','r') as f:
    text = f.read();
lst = text.replace('\n',' ').split('.')
try:
    lst.remove('')
except Exception as e:
    errors = "Last letter havn't dot"
words = text.replace('\n',' ').replace('(',' ').replace(')',' ').replace('—',' ').replace(',',' ').replace('.',' ').replace('-',' ').replace(':',' ').split()

lett = []
for i in words:
    for j in i:
        lett.append(j)

print('List:' + str(len(lst)))
print('Words:' + str(len(words)))
print('Letters:' + str(len(lett)))
print('Avg list length: ' + str(len(words)/(len(lst))))
print('Avg word length: ' + str(len(lett)/len(words)))

alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9')
parse = []
for i in range(0,len(alphabet)):
    parse.append(0)
    for j in lett:
        if j == alphabet[i]:
          parse[i] += 1

alphaDic = {}
for i in range(0, len(alphabet)):
    alphaDic[alphabet[i]] = str(float("{0:.1f}".format((parse[i]/len(words))*100))) + '%'
print(alphaDic)

with open('result.txt','w') as out:
    out.write('List:' + str(len(lst)) + '\n')
    out.write('Words:' + str(len(words)) + '\n')
    out.write('Letters:' + str(len(lett)) + '\n')
    out.write('Avg list length: ' + str(len(words)/(len(lst))) + '\n')
    out.write('Avg word length: ' + str(len(lett)/len(words)) + '\n')
    out.write('Leter and numbers frequency:' + '\n')
    out.write(str(alphaDic))