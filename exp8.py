# Open input file in read mode
input_file = open("input.txt", "r")

# Read all lines
lines = input_file.readlines()

# Count the number of lines
line_count = len(lines)

# Extract the first two lines
first_two_lines = lines[:2]

# Open output file in write mode
output_file = open("output.txt", "w")

# Write the first two lines to output file
output_file.writelines(first_two_lines)

# Close both files
input_file.close()
output_file.close()

# Display the number of lines
print("Number of lines:", line_count)
print("First two lines have been written to output.txt")