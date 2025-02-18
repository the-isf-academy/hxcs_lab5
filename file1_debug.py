# /////////// INSTRUCTIONS /////////////////
# 🧐 What do you think will happen when you run this code? 

# 💻 Run the file and debug the code 
#    - this file has 3 bugs 
#    - Fix all 3 bugs
#    - read the output to make sure the print statements make sense 

# ////////////////////////////////////////////


from random import randint 

print("--- 🎲 Welcome to the Number Guessing Game 🎲 ---\n")

random_number = randint(1,10)      

for i in range(4) 

    user_guess = int(input("Guess a number bewtween 1-10: "))

    if user_guess = random_number: 
        print(f"👏 Correct - you win!\n")

    elif user_guess > random_number:
        print(f" ...too high\n")  

    elif user_guess < random_number:
        print(f"...too low")


  
if user_guess != random_number:
  print(f"😢 You won!")
