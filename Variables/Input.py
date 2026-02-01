# 1. Python asks a question and waits
favorite_language = input("What language are you learning? ")

# 2. It stores your answer in the variable
print("That's right! " + favorite_language + " is the best choice.")

# 3. Let's try a number
age = input("How many years old are you? ")

# This next line will work because we are just printing text
print("You are " + age + " years old.")

#Study Calculator
name = input("What is your name? ")
daily_goal = input("How many hours do you want to study each day? ")
int(daily_goal)
weekly_total = int(daily_goal) * 7
print("Hey " + name + "," + " If you study that much, you will hit " + str(weekly_total) + " hours a week!")
