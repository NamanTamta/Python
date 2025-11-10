import random

# Define character sets
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+{}|:<>?-=[];',./`~"

# Combine all character sets
allchar = upper + lower + numbers + symbols

# Get desired password length from user
length = int(input("Enter the length of the password: "))

# Generate password
password = " "

# Loop to create password of specified length
for a in range(length):
    password += random.choice(allchar) # password = password + random character from allchar
print("Your generated password is: ", password)