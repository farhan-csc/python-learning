# operation of string: len(), .upper(), .lower(), .strip(), replace(old, new), startswith(...)
name = " Muhammad Farhan "
message = "I am learning Python"

print(f"Displaying the length of the name: {len(name)}")
print(f"Convert the message to uppercase: {message.upper()}")
print(f"Convert the message to lowercase: {message.lower()}")
print(f"Remove spaces: {name.strip()}")
print(f"Replace text: {message.replace('Python', 'AI')}")
print(f"Start with: {message.startswith('I am')}")

print(f"\n{name}")
print(name.strip())
print(len(name))
print(len(name.strip()))