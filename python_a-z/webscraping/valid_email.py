import re

email ="bons6710gmail.com"
pattern= r".+\@.+\..+"
if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")
    
if re.search(pattern, email):
    print("Pattern found in the email address!")
else:
    print("Pattern not found in the email address.")