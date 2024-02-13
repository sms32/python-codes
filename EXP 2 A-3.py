contacts = []
for i in range(5):
    name,number = input("Enter contact details :").split()
    contacts.append((name,number))
search_name = input("Enter name :")
for name , number in contacts:
    if name== search_name:
        print("Mobile number is",number)
        break
    else:
        print("contact not found")
