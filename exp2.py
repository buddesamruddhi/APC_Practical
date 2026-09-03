#1

# n= int (input("enter the natural numbers: "))
# for i in range (1, n+1):
#     print(i)

#2
# n=int(input("enter the number"))
# if n % 2==0:
#     print("the number is even")

#3
# n= int(input("enter the number "))
# if n%2 !=0:
#     print("the number is odd")

#4
# n= int(input("enter the number"))
# for i in range(n):
#     print(2**i)


# #11
# n= int(input("enter the number"))
# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()

# #12
# n= int(input("enter the number"))
# for i in range (1,n+1):
#     for j in range (1, i+1):
#         print(i,end="")
#     print()

#8
# for i in range (1,4):
#     for j in range (1,4):
#         if(j==1):
#             print("A", end=" ")
#         elif(j==2):
#             print("B", end=" ")
#         else:
#             print("C", end=" ")
#     print()


# #while loop
#1
# n=int (input("enter the number"))

# i=1
# while i<=n:
      
#     print(i)
#     i=i+1

#2
# n= int(input("enter the number"))
# i=1
# while i<=n:
#     if i%2==0:
#         print(i)
#     i=i+1

#3
# n= int(input("enter the num"))
# i=2
# while i<=n:
#     print(i)
#     i=i+1


#3

# n=int(input("enter the no"))
# i=1
# while i<=n:
#     print(i)
#     i=i+2


n= int(input("enter the no"))
i=1
sum=0

while i<=n:
    sum=sum+i
    print(i)

    i=i+1
print("sum of natural numbers is:", sum)