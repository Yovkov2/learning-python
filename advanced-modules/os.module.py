import os

for filename in os.listdir('.'):
    if os.path.isfile(filename):
        size = os.path.getsize(filename)
        print(f"{filename} - {size} bytes")
