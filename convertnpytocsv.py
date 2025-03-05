import numpy as np
import pandas as pd

# Load the .npy file
npy_file = 'sample_data.npy'  # Replace with your .npy file path if different
data = np.load(npy_file)
print("Loaded array from .npy:")
print(data)

# Convert the NumPy array to a pandas DataFrame
df = pd.DataFrame(data)
print("\nConverted to DataFrame:")
print(df)

# Save the DataFrame to a .csv file
csv_file = 'output_data.csv'  # Name of the output CSV file
df.to_csv(csv_file, index=False)
print(f"\nArray saved as '{csv_file}'")