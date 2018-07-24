str =input('Enter String: ')
words =str.split()
dic={}
for word in words:
    if(word[0] not in dic.keys()):
        dic[word[0]]=[]
        dic[word[0]].append(word)
    else:
        if(word not in dic[word[0]]):
          dic[word[0]].append(word)
print(dic)