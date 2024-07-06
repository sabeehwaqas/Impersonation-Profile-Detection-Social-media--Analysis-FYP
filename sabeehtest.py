
import json
import os

def Jsonmaker(new_data):

    # Define the path and filename of the JSON file
    filename = "dataofprediction.json"
    path = "D:\\twitterprofiles\\"

    # Check if the file exists, if not, create it
    if not os.path.exists(os.path.join(path, filename)):
        with open(os.path.join(path, filename), "w") as f:
            json.dump([], f)

    # Load the existing data from the file
    with open(os.path.join(path, filename), "r") as f:
        data = json.load(f)

    # Clear the data in the file if it contains any
    if data:
        data.clear()

    # Append new data to the list of dictionaries
    #new_data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
    data += new_data

    # Write the updated data to the file
    with open(os.path.join(path, filename), "w") as f:
        json.dump(data, f)
