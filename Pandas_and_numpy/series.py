
import pandas as pd
from pathlib import Path

# Read the CSV file
folder = Path(__file__).parent
data = pd.read_csv(folder / "students.csv")

# Create a Series
s = pd.Series(data["Marks"])

# Display the Series
print("Pandas Series:")
print(s)