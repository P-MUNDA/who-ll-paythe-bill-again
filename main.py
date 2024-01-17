# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#METHODE@1

import random
length_names=len(names)
print(length_names)
print(names)
person_to_pay=random.randint(0,int(length_names)-1)
if person_to_pay==0:
  print(f"Today {names[0]} will pay all our bill !")
else:
  print(f" Today {names[person_to_pay]} will pay the bills !")


#METHODE@2
print(f" {names[person_to_pay]} is going buy the meals today")

#METHODE 3
person_to_paybills=random.choice(names)
print(f"Tt is {person_to_paybills}, who will pay.")




