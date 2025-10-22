import re

text = "Contact us at info@hogwarts.edu or help@magic.co.uk"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(emails)
