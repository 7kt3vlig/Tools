import re

def find_inc_codes(filename):
    # Define the regex pattern to match "INC" followed by exactly 7 digits
    pattern = r'\bINC\d{7}\b'

    # Initialize an empty list to store matches
    matches = []

    # Open the file and read its content with the correct encoding
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

            # Find all occurrences of the pattern in the text
            matches = re.findall(pattern, text)
    except UnicodeDecodeError as e:
        print(f"Error decoding the file: {e}")
        return []

    return matches

# Example usage
filename = r'C:\Users\Jag\Desktop\cristina.txt'  # Correct file path
matches = find_inc_codes(filename)

# Print the matches and their count
if matches:
    print(f"Matches found: {matches}")
    print(f"Total matches: {len(matches)}")
else:
    print("No matches found")