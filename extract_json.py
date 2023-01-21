import os
import json

# specify the directory where the files are located
dir_path = './images'
os.makedirs(dir_path, exist_ok=True)

# create a new directory to store the json files
json_dir_path = './json'
os.makedirs(json_dir_path, exist_ok=True)

# initialize a counter for the file names
counter = 1

# loop through all the files in the directory
for file in os.listdir(dir_path):
    # get the file name without the extension
    file_name = os.path.splitext(file)[0]

    # remove the first 30 characters from the file name
    file_name_modified = file_name[30:]

    # split the file name at the underscore, if present
    if '_' in file_name_modified:
        artist, quote = file_name_modified.split('_', 1)
    else:
        artist = file_name_modified
        quote = ''

    # remove the last 36 characters from the quote, if present
    if len(quote) > 36:
        quote = quote[:-37]

    # create the content to be written to the json file
    content = {
            "attributes": [
                {
                  "trait_type": "Artist",
                  "value": artist
                }
            ],
            "unlockable_content": [
                True,
                f"Artist Name = {artist} \r\n The Imagination Quote = {quote}"
            ]          
        }

    # Format the JSON data
    formatted_json = json.dumps(content, indent=2)

    # create the full path to the json file with the new file name
    json_file_path = os.path.join(json_dir_path, f'{counter}.json')

    # open the json file for writing
    with open(json_file_path, 'w') as json_file:
        # write the formatted content to the json file
        json_file.write(formatted_json)

    # increment the counter
    counter += 1

print('Done!')
