
import numpy as np

# Create an array of values
arr = np.array([85, 90, 78, 92])

# Create character labels
labels = np.array(['A', 'B', 'C', 'D'])

# Display the array
print("Original Array:")
print(arr)

# Display character labels
print("Character Labels:")
print(labels)

# Display labels with array elements
print("Labels with Values:")
for i in range(len(arr)):
    print(labels[i], ":", arr[i])