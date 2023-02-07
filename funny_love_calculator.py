print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

all_string = name1 + name2
lower_case = all_string.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
love = l + o + v + e

love_score = str(true) + str(love)
int_love_score = int(love_score)

if 10 > int_love_score or int_love_score > 90:
  print(f"Your score is {int_love_score}, you go together like coke and mentos.")
elif 40 <= int_love_score <= 50:
  print(f"Your score is {int_love_score}, you are alright together.")
else:
  print(f"Your score is {int_love_score}.")
