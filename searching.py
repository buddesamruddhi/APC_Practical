n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter a number: ")))

target = int(input("Enter the element to search: "))

if target in arr:
    print("Element found")
else:
    print("Element not found") 