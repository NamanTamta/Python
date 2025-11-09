import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+{}|:<>?-=[];',./`~"
allchar = upper + lower + numbers + symbols
length = int(input("Enter the length of the password: "))
password = " "
for a in range(length):
    password += random.choice(allchar)
print("Your generated password is: ", password)