import re

def find_inc_codes(filename):
    """Extract all words starting with 'INC' followed by 7 digits from a given file."""
    # Define the regex pattern to match "INC" followed by exactly 7 digits
    pattern = r'\bINC\d{7}\b'

    # Initialize an empty list to store matches
    matches = []

    # Open the file and read its content
    with open(filename, 'r') as file:
        text = file.read()

        # Find all occurrences of the pattern in the text
        matches = re.findall(pattern, text)

    return matches

def find_duplicates(list1):
    """Find duplicates within a single list."""
    # Use a set to store seen items and a set to store duplicates
    seen = set()
    duplicates = set()

    for item in list1:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

# Example usage
filename = r'C:\Users\Jag\Desktop\cristina2.txt'  # File path

# Find all 'INCxxxxxxx' codes in the file
matches = find_inc_codes(filename)

# Find duplicates within the list of matches
duplicates = find_duplicates(matches)

# Print the results
print(f"Total matches found: {len(matches)}")

if duplicates:
    print(f"Duplicates found: {duplicates}")
    print(f"Total duplicates: {len(duplicates)}")
else:
    print("No duplicates found")

# Optionally, print all matches (if you want to see them)
#print(f"Matches found in {filename}: {matches}")