num_input = int(input())

while num_input!=0:
  word = input()
  final_word = ''
  if len(word)>10:
    final_word = word[0] + str(len(word)-2) + word[-1]
    print(final_word)
  else:
    final_word = word
    print(final_word)
  num_input -=1
