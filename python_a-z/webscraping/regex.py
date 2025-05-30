import re

pattern = "^h"
text = "hello world"
# Check if the pattern matches the beginning of the text

if re.match(pattern, text):
    print("Match found!")
else:
    print("No match found.")
    
# search_pattern = "world"
# Search for the pattern in the text
search_pattern = "worlds"
if re.search(search_pattern, text):
    print("Pattern found in the text!")
else:
    print("Pattern not found in the text.")