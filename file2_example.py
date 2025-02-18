# /////////// INSTRUCTIONS /////////////////

#  📖 In the next file we will create a typing game. 
#       - we will need to compare two sentences to analyze how similar they are 

# 1️) 💻 Run the file 

# 2️) 💻 Experience with changing the sentences

# ////////////////////////////////////////////

import difflib

sentence1 = "peanut butter is yummy"
sentence2 = "peanut butter is bad"

similarity_ratio = difflib.SequenceMatcher(None, sentence1, sentence2).ratio()

similarity_percentage = round(similarity_ratio * 100, 2) # converts ratio to a percentage

print(f"sentence 1: {sentence1}")
print(f"sentence 2: {sentence2}")
print(f"Similarity ratio: {similarity_percentage}% ")