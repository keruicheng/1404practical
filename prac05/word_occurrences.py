string = input("Text:").strip()
count_dic = {}

for word in string:
    freq = count_dic.get(word, 0)
    count_dic[word] = freq + 1

word = list(count_dic.keys())
string.sort()

max_length = max((len(word) for word in string))
for word in string:
    print("{:{}} : {}".format(word, max_length, count_dic[word]))

