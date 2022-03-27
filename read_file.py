import jieba

f_name = 'info.txt'

with open(f_name, encoding='utf-8') as a:
    b = a.read()

words = jieba.lcut(b)

count = {}

for word in words:
    if len(word) < 2:
        continue
    else:
        count[word] = count.get(word, 0) + 1

list1 = list(count.items())
list1.sort(key=lambda x: x[1], reverse=True)

for i in range(10):
    word, number = list1[i]
    print("Keyword:{:-<10} : {:+>8}".format(word, number))
