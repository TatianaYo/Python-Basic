# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.


s = '''Emancipation generally means to free a person from a previous restraint or legal disability.
    More broadly, it is also used for efforts to procure economic and social rights, political rights or equality, often for a 
    specifically disenfranchised group, or more generally, in discussion of many matters.
    Among others, Karl Marx discussed political emancipation in his 1844 essay "On the Jewish Question", 
    although often in addition to (or in contrast with) the term human emancipation. 
    Marx's views of political emancipation in this work were summarized by one writer as entailing 
    "equal status of individual citizens in relation to the state, equality before the law, regardless of religion, property,
    or other "private" characteristics of individual people."'''
punct = ',.!?:;"()'

#list1 = [word.rstrip(punct) for word in s.split() if len(word.rstrip(punct)) > 1]
#print(*sorted(set(list1), key=list1.count, reverse=True)[:10], sep='\n')



res = len(s.split())
print('Количество слов = ', + res)
s = s.split()
#print(s)
for word in s:
    if len(word.rstrip(punct)) > 1:
        word.rstrip(punct)
print(*sorted(set(s), key=s.count, reverse=True)[:10], sep='\n')