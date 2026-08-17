# text='samruddhi'
# print(text)

# text="hiii.......whats up"
# print(text)

# text='''hello .. my name is samruddhi 
# i am from kolhapur'''
# print(text)



#String

#1
# text=input("enter teh string ")
# count = 0
# for i in text:
#     count = count+1
# print("lenght of the string is :",count)

#2
# text= input("enter the string")
# vowels=0
# consonants=0
# digits=0
# space=0
# special_characters=0

# for i in text:
#     if i in "aeiou||AEIOU":
#         vowels=vowels+1
#     elif ('a'<= i <='z' or 'A'<=i <='Z'):
#         consonants = consonants +1
#     elif i>='0'and i<='9':
#         digits=digits+1
#     elif i==' ':
#         space=space+1
#     else:
#         special_characters=special_characters+1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Spaces:", space)
# print("Special Characters:", special_characters)


#3
# text= input("enter the string ")
# reverse=""
# for i in text:
#     reverse= i+reverse 
# print("reverse:", reverse)

#4
# text = input("enter the string:")
# reverse =""
# for i in text:
#     reverse = i + reverse
# if text ==  reverse:
#         print("the string is palindrome ")
# else:
#         print("not palindrome")


#5
# text = input("Enter the string: ")

# upper = 0
# lower = 0

# for i in text:
#     if 'a' <= i <= 'z':
#         lower += 1
#     elif 'A' <= i <= 'Z':
#         upper += 1

# print("Upper case:", upper)
# print("Lower case:", lower)


#11

# text = input("enter the statement:")
# count =0
# for i in text:
#     count = count + 1
# print("length of the statement characters is :",count)


#

# text= input("enter the string:")
# result = ""
# for i in text:
#     if i != " ":
#         result = result +i
    
# print("string without spaces:", result)

# text = input("Enter a string: ")

# for i in range(len(text)):
#     count = 0

#     for j in range(len(text)):
#         if text[i] == text[j]:
#             count += 1

#     if count > 1:
#         duplicate = False

#         for k in range(i):
#             if text[i] == text[k]:
#                 duplicate = True
#                 break

#         if not duplicate:
#             print(text[i])

