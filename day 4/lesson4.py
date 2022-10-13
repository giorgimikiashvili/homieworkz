# a=5

# print(a//2)

# my_name = "nika"

#iteration - იტერაცია - განმეორება

#ამ შემთხვევაში char არის საიტერაციო ცვლადი

# for char in my_name:
#     print(char)
    
#i არის საიტერაციო ცვლადი ამ შემთხვევაში

# for i in range(10):
#     print(str(i) + "a")




name1 = input("enter name1: ")
name2 = input("enter name2: ")

amount_vowels_in_name1 = 0
amount_vowels_in_name2 = 0

for char in name1:
    if char in "aeiou":
        amount_vowels_in_name1 += 1
for char in name2:
    if char in "aeiou":
        amount_vowels_in_name2 += 1

if amount_vowels_in_name1 > amount_vowels_in_name2:
    print("the amount of vowels in name 1 is more and it contains {} vowels".format(amount_vowels_in_name1))
elif amount_vowels_in_name1 < amount_vowels_in_name2:
    print("the amount of vowels in name 2 is more and it contains {} vowels".format(amount_vowels_in_name2))
else:
    print("they have equal amount of vowels")