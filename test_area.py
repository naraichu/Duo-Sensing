import json
import random
import time

# File path that JSON is stored
file_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Arduino_Software/Duo_Tactile_Software/ML/datasets.json"

try:
    # Add opening square bracket "[" at the start of the file
    with open(file_path, "a") as f:
        f.write("[")


    while True:
        data = random.randint(0, 100)

        dictionary = {
            "action": "None",
            "sfcs_value": [
                random.randint(0, 100) for _ in range(10)
            ],
        }

        with open(file_path, "a") as f:  # Open file in append mode
            if f.tell() > 1:  # If not the first element, add a comma before appending
                f.write(",\n")
            json.dump(dictionary, f, separators=(",", ":"))
            f.write("\n")
        
        time.sleep(0.5)  # Add a delay of 0.5 seconds

except KeyboardInterrupt:
    # Add closing square bracket "]" when keyboard interrupt occurs
    with open(file_path, "a") as f:
        f.write("\n]")
