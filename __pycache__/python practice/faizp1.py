import pandas as pd
import csv
# Create Dataset
data = {
    "ID": [1, 2, 3, 4],
    "Name": ["Ali", "Sara", "John", "Emma"],
    "Age": [20, 21, 22, 23]
}

df = pd.DataFrame(data)

# Delete one row
df = df.drop(1)

# Delete one column
df = df.drop("Age", axis=1)

# Add two columns
df["City"] = ["Delhi", "Mumbai", "Lucknow"]
df["Marks"] = [85, 90, 88]

# Add two rows
new_rows = pd.DataFrame({
    "ID": [5, 6],
    "Name": ["David", "Sophia"],
    "City": ["Kanpur", "Agra"],
    "Marks": [92, 95]
})

df = pd.concat([df, new_rows], ignore_index=True)

# Convert DataFrame to CSV file
df.to_csv("student_data.csv", index=False)

print("CSV file created successfully!")

