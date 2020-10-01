import re, random, string
from pprint import pprint

#---------compiling a frequency table for full War'n'Peace book-----------
f_table_full = {'а':0, 'б':0, 'в':0, 'г':0, 'д':0, 'е':0, 'ё':0, 'ж':0, 'з':0, 'и':0, 'й':0, 'к':0,
      'л':0, 'м':0, 'н':0, 'о':0, 'п':0, 'р':0, 'с':0, 'т':0, 'у':0, 'ф':0, 'х':0, 'ц':0,
      'ч':0, 'ш':0, 'щ':0, 'ъ':0, 'ы':0, 'ь':0, 'э':0, 'ю':0, 'я':0,}

b = open("wnp_full.txt")
book = list(b.read())
b.close()

def count(book):
    count = 0
    for word in book:
        if word in f_table_full.keys():
            count += 1
    return(count)
allw=count(book)

def similar(book,f_table_full,allw):
    for i in f_table_full.keys():
        count = 0
        for word in book:
            if i == word:
                count += 1
                f_table_full[word] = count/allw
    return(f_table_full)

full_b = similar(book,f_table_full,allw)#frequency table of full book

#----------encrypting one chapter from War'n'Peace------------

a = open("wnp_ch.txt", "r")
ch = list(a.read().lower())
a.close()


alphalbet = [c for c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя']
key = random.randint(0,32)
print(key)
a=0
for i in ch:
    if i in alphalbet:
        ch[a] = alphalbet[alphalbet.index(i) + key]
    a += 1
ch = ''.join(ch)
with open('encrypted.txt','w') as enc_file:
    enc_file.write(ch)

#---------compiling a frequency table for one chapter of War'n'Peace book-------

allw=count(ch)

f_table_ch = {'а':0, 'б':0, 'в':0, 'г':0, 'д':0, 'е':0, 'ё':0, 'ж':0, 'з':0, 'и':0, 'й':0, 'к':0,
      'л':0, 'м':0, 'н':0, 'о':0, 'п':0, 'р':0, 'с':0, 'т':0, 'у':0, 'ф':0, 'х':0, 'ц':0,
      'ч':0, 'ш':0, 'щ':0, 'ъ':0, 'ы':0, 'ь':0, 'э':0, 'ю':0, 'я':0,}

ch_b = similar(ch,f_table_ch,allw)#frequency table of one chapter book

#---------sorting and matching frequency tables------------

# pprint(f_table_full)
# print("------")
# pprint(f_table_ch)

list_c = list(ch_b.items())
list_c.sort(key=lambda i: i[1])
dict_numbers = {}
for i in list_c:
    dict_numbers[i[0]] = i[1]
#print(dict_numbers)
list_b = list(full_b.items())
list_b.sort(key=lambda i: i[1])
dict_full = {}
for i in list_b:
    dict_full[i[0]] = i[1]
a = []
for n in dict_full.keys():
    a.append(n)
ch = ''.join(ch)
count = 0
print(str(a[0]))
#print(dict_numbers[1])
print(dict_full,'\n',a,'\n',dict_numbers)
for i in dict_numbers.keys():
    print(i,a[count],type(i),type(a[count]))
    ch = ch.replace(i,a[count])
    count += 1
with open('decrypted.txt', 'w') as dec_file:
    dec_file.write(ch)
