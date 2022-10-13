#ინფუთით შეიტანეთ თქვენი სახელ იდა გვარი,
#ტერმინალში გამოიტანეთ რომელ ინდექსზე არის ხმოვნები

#nika keshelava

# from re import A


# 1 - i

# 3 - A

# 6 - e

#while, [i], in, "aeiou"

# full_name = input("enter your full name: ")

# i = 0
# while i < len(full_name):
#     if full_name[i] in "aeiou":
#         print(str(i) + full_name[i])
        
#     i =+ 1
    
    
    
full_name = input("enter your name: ")

i = 0

while i < len(full_name):
    if full_name[i] in "aeiou":
        print(str(i) + full_name[i] )
    i += 1