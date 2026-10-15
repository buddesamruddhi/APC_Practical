import os

os.mkdir("Directory1")
print("Directory created successfully")


print("\nCurrent working directory:")
print(os.getcwd())

# 3. Get the list of contents present in the directory
print("\nContents of current directory:")
print(os.listdir())

# 4. Rename the directory
os.rename("Directory1", "Directory2")
print("\nDirectory renamed successfully")

# 5. Change the current working directory
os.chdir("Directory2")
print("\nChanged current working directory to:")
print(os.getcwd())

# 6. Get the list of contents in the current directory
print("\nContents of Directory2:")
print(os.listdir())

# 7. Change back to the parent directory
os.chdir("..")
print("\nChanged back to parent directory:")
print(os.getcwd())

# 8. Remove the directory
os.rmdir("Directory2")
print("\nDirectory removed successfully")