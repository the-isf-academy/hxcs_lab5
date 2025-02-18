import string

# /////////// INSTRUCTIONS /////////////////
# 🎲 Let's make a password strength program 
#     - it will tell the user if their password is weak, medium, or strong 
#
# weak password
#   - less than 8 letters 
#   - does not contain a number
#   - does not contain an uppercase letter 
#
# medium password
#   - has more than 8 letter
#   - 

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


if len(password) < 8:
    print(f"Weak")

has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special_char = any(char in string.punctuation for char in password)

if has_uppercase and has_lowercase and has_digit and has_special_char:
    print(f"strong")
elif has_uppercase and has_lowercase and (has_digit or has_special_char):
    print(f"medium")
else:
    print(f"weak")


    