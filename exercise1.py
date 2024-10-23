# Initialize an empty dictionary
phone_book = {}

# Predefined 5 names and phone numbers
entries = [
    ("Justin", "123-456-7890"),
    ("Chellshe", "234-567-8901"),
    ("Tiara", "345-678-9012"),
    ("Laura", "456-789-0123"),
    ("Michelle", "567-890-1234")
]

# Add the entries to the dictionary
for name, phone_number in entries:
    phone_book[name] = phone_number

# Search for a name
search_name = "Justin"  # You can change this to test with other names

# Search and print result
if search_name in phone_book:
    print(f"{search_name}'s phone number is: {phone_book[search_name]}")
else:
    print(f"Error: {search_name} not found in the phone book.")