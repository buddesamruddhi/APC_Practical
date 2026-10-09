
import pandas as pd
from pathlib import Path

# Get the folder containing this Python file
folder = Path(__file__).parent

# Read data from the CSV file
data = pd.read_csv(folder / "students.csv")

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Student DataFrame:")
print(df)