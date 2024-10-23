phonebook = {}

for i in range(5):
    name = input("Enter name: ")
    phone  = input("Enter phone number: ")
    phonebook[name] = phone 

name = input("input a name to search")
if name in phonebook.keys():
    print(phonebook[name])
else:
    print("name not found")  # Output: name not found