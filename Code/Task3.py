import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 15, 10, 40, 25, 30]
}
df = pd.DataFrame(data)

# Define a custom function to transform each group
def custom_transform(group):
    # Example: normalize values within each group by the group's mean
    group['Normalized'] = group['Values'] / group['Values'].mean()
    return group

# Apply the custom transformation using groupby and apply
result = df.groupby('Category').apply(custom_transform)

print("Original DataFrame:\n", df)
print("\nTransformed DataFrame:\n", result)
