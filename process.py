# Read in the file
with open('chapter2.txt', 'r') as file:
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('“', '"')
filedata = filedata.replace('”', '"')

# Write the file out again
with open('chapter2_format.txt', 'w') as file:
  file.write(filedata)