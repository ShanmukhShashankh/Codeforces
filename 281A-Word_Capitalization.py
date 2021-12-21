word = input()
word_list = []
final_word = ''
for i in word:
  word_list.append(i)
word_list[0] = word_list[0].upper()
for i in word_list:
  final_word += i
print(final_word)