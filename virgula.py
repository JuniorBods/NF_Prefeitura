# Open input file for reading
with open("Bradesco_02052022_102734.OFX", "r") as input_file:
    # Read entire contents of file into a string
    contents = input_file.read()

# Replace commas with periods
contents = contents.replace(",", ".")

# Open output file for writing
with open("Bradesco_02052022_102734.OFX", "w") as output_file:
    # Write contents of file
    output_file.write(contents)