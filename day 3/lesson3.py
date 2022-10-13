# my_sentence = "aa {0} bb {1} ".format ("zz", "yy")

# print(my_sentence)


# if False:
#     print("10")
# else:
#     print("20")
    
# #print - output
# #input() - input

# my_age = input("how old are you:")

# print("")

# # age = 22
# # age += 5  #gazrda

# #print(age)

# a = "20"  #stringebi miecepeba
# b = "30"
# c = "40"


# ricxvi1 = input("sheiyvanet pirveli ricxvi:")
# ricxvi2 = input ("sheikvanet meore ricxvi:")


# jami = int(ricxvi1) + int(ricxvi2)

# print(jami)

# num1 = int(input ("sheikvanet pirveli ricxvi:"))
# num2 = int(input ("sheikvanet meore ricxvi:"))

# sum = num1 * num2

# if num1*num2>100 in sum:
#     print("xxx")
# else:
#     print("yyy")
    

# a = 4
# b = 3


# print(a + b)
# print(a * b)
# print(a / b)
# print(a - b)
# print(b % a) #ramdeni darcheba nashti

# print(a ** b) #xarisxshi akvana

# print(a // b)
# print(a / b)




# num1 = int(input ("sheikvanet pirveli ricxvi:"))
# num2 = int(input ("sheikvanet meore ricxvi:"))
# num3 = int(input ("sheikvanet mesame ricxvi:"))

# product = num1 + num2 + num3 

# if (num1 % 2) == 0:
#     print("Even")
# else:
#     print("Odd")


num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))
num3 = int(input("enter number2: "))
my_sum = 0

if num1 % 2 ==1:
    my_sum += num1
    
if num2 % 2 ==1:
    my_sum += num2
#my_sum = 13    
if num3 % 2 ==1:
    my_sum += num3

#my_sum-ს რომელიც ბოლო ვერსიის მიხედვით უდრიდა 13-ს, კიდევ დაემატა 5, გახდა 18

print("the sum of odd numbers is{}".format(my_sum))