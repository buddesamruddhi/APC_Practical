# file=open("data.txt","r")
# print("\nData using read() method:")
# data = file.read()
# print(data)

# file.close()

# file = open("data.txt", "r")

# print("Data using readline() method:")
# print(file.readline())
# print(file.readline())

# file.close()

file = open("data.txt", "r")

print("Data using readlines() method:")
lines = file.readlines()
print(lines)

file.close()