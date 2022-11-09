input_str = input('jgseijg: ')
words_list = input_str.split()
word_key = {}
for word in words_list:
    word_key[word] = len(words_list)


print(word_key)
