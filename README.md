# npy-to-csv Converter

## Overview
This Python script converts a `.npy` file (NumPy array) into a `.csv` file using NumPy and Pandas. It loads the `.npy` file, converts it into a Pandas DataFrame, and then saves it as a `.csv` file.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install numpy pandas
```

## Usage
1. Place your `.npy` file in the same directory as the script.
2. Update the script with the correct `.npy` file path if needed.
3. Run the script using:

```bash
python convertnpytocsv.py
```

## Code Example
```python
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
```

## Output
After running the script, the `.csv` file will be created in the same directory with the specified name.

## Notes
- Ensure that the `.npy` file contains structured data that can be represented as a DataFrame.
- Modify the `csv_file` variable if you want to change the output file name.

## License
This script is provided under the MIT License.

