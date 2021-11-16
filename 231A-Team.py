num_input = int(input())
answered = 0

while num_input!=0:  
  final_number = 0
  number  = input()
  number  = number.split()
  for i in number:
    final_number += int(i) 
  if final_number>=2:
    answered += 1
  num_input -=1
  
print(answered)
