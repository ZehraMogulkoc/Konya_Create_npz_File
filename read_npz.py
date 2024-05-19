import numpy as np

# Load the .npz file
data = np.load(r'C:\Users\Lenovo\OneDrive\Masaüstü\konya_kavşak.npz')

# Print the names of arrays stored in the .npz file
print("Arrays in the .npz file:", data.files)

# Print the first 10 lines of each array
for key in data.files:
    print(f"Shape of '{key}' array:", data[key].shape)
    
for key in data.files:
    print(f"Array '{key}':")
    print(data[key][:10])  # Print the first 10 lines

output_file = 'output.txt'

# Open the file in write mode
with open(output_file, 'w') as f:
    # Print the names of arrays stored in the .npz file
    f.write("Arrays in the .npz file: " + str(data.files) + "\n\n")

    # Print the first 10 lines of each array
    for key in data.files:
        f.write(f"Array '{key}':\n")
        # Iterate through the first 10 elements of the first axis
        for i in range(min(10, data[key].shape[0])):
            np.savetxt(f, data[key][i])
            f.write("\n")