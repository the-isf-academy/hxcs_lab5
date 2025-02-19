# /////////// INSTRUCTIONS /////////////////
# 🎲 Let's make a typing test!

# 💻️⃣ Run the file to see how it works. 
#     It's up to you to finish the game!
#
# Extension ideas: 
#   - add words per minute 
#       - tell the user their WPM
#
#   - add difficulty settings
#       - easy, medium, hard 

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

from random import choice
from time import time 
import difflib


sentence_list = [
    "the quick brown fox jumped over the lazy dog",
    "hello this is your captain speaking"
]


## print rules 

print(f"--- ⌨️ Welcome to the Typing Test ⌨️ ---\n")
print(f"     1. You will see the prompt")                       
print(f"     2. The timer will start")
print(f"     3. Type the prompt as fast as you can")
print(f"     4. Click 'enter/return' when you are done.\n")
input("> Input any key to start the game! ")  

## game logic

start_time = time()    # store start time 

# ⬇️💻️ create a varible that stores a random sentence from sentence_list



user_test = input("") # stores the user input typing test

end_time = time()   # store end time
 
# ⬇️💻️ fix the calculation of the total_time 
total_time = 0 

# ⬇️💻️ print the total_time, so the user knows how many seconds it took them to type



# ⬇️💻️ use the example from file2_example.py 
#     to calcaulte the accuratacy percentage of the user_test
#     then, print the accuracy
