import json

# Load the JSON data from the file
with open('collection_scarp_data_from _opensea.json', 'r') as f:
    data = json.load(f)

# Extract the "nft_url" and "nft_name" values from the data
extracted_data = [{'nft_url': item['nft_url'], 'nft_name': item['*nft_name']} for item in data['nft']]

# Save the extracted data to a new file
with open('nft_urls_for_twitter', 'w') as f:
    json.dump(extracted_data, f)
