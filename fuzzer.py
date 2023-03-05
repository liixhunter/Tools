import requests

# Set the target URL
target_url = "https://example.com/login"

# Set the input field to fuzz
input_field = "comment"

# Load the wordlist
with open("payloads.txt", "r") as f:
    wordlist = f.read().splitlines()

# Loop through the wordlist and fuzz the input field
for word in wordlist:
    # Construct the payload
    payload = {input_field: word}

    # Send the request
    r = requests.post(target_url, data=payload)

    # Check the response for signs of success or failure
    if "Login successful" in r.text:
        print(f"SUCCESS: '{word}'")
    elif "Invalid username" in r.text:
        print(f"FAILURE: '{word}'")
    else:
        print(f"UNKNOWN: '{word}'")
