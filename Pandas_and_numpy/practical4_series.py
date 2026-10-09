
import pandas as pd
from pathlib import Path

# Get the folder containing this Python file
folder = Path(__file__).parent

# Read the CSV file from the same folder
data = pd.read_csv(folder / "students.csv")

# Create a Series
marks_series = pd.Series(data["Marks"])

# Display the Series
print("Student Marks Series:")
print(marks_series)