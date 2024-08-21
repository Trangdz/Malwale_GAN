# Code example for reading a .npz file using numpy

# Import numpy library
import numpy as np

# Define the path to the .npz file
npz_file_path = 'path_to_your_npz_file/data.npz'

# Load the .npz file
npz_data = np.load(npz_file_path, allow_pickle=True)

# Print the keys of the .npz file
print("Keys of the npz file:", npz_data.files)

# Print the contents of each file within the .npz file
for file in npz_data.files:
    print(f"Contents of the file '{file}':")
    print(npz_data[file])
