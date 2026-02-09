from setuptools import find_packages

# Look for packages inside src/
found = find_packages(where="src")
print("Found packages:", found)