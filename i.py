import random
with open('hi.txt') as f:lines = f.readlines()
for i in range(len(lines)):lines[i] = lines[i].replace('\n', '')
used_letters, word, good_letters, hi= [],random.choice(lines), 'qwertyuiopasdfghjklzxcvbnm', 1;chosen = "-" * len(word)
while True:
  try:
    hi = int(input("How many tries? : "));
    if hi > 10:
      continue;
    break
  except:print("What is wrong with you")
print(f"Length is {len(word)}")
while word != chosen:
  if hi == 0:print("You are so bad");print(word);exit()
  you, used = "HEYYYYY", 0;print(chosen);print("Letters used:", used_letters);print(f"You have {hi} tries left!")
  while len(you) != 1 or you in used_letters or you not in good_letters:you = input("Which letter do you write? :").lower()
  used_letters.append(you)
  for i in range(len(word)):
    if word[i] == you:string_list = list(chosen);string_list[i] = you;chosen = "".join(string_list);used += 1
  if used == 0:hi -= 1
print(f"The word is {word}! You got it!")