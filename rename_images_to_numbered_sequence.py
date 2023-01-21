import os

# Set the directory of the files to be renamed
directory = './images'

# Get a list of all the files in the directory
files = os.listdir(directory)

# Iterate over the files in the directory
for i, file in enumerate(files, start=1):
  # Get the file name and extension
  name, extension = os.path.splitext(file)

  # Construct the new file name with the sequential number
  new_name = str(i) + extension

  # Rename the file with the new name
  os.rename(os.path.join(directory, file), os.path.join(directory, new_name))

print('Done!')
