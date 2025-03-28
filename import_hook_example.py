# import_hook_example.py
import pandas as pd  # This now uses FireDucks under the hood

# Create a sample DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'salary': [50000, 60000, 75000, 90000]
})

# Perform operations
filtered_df = df[df['age'] > 30]
grouped = df.groupby('age')['salary'].mean()

print("Filtered DataFrame:")
print(filtered_df)
print("\nGrouped Salary by Age:")
print(grouped)
