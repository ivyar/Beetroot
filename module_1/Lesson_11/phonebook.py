import json

def search(data, key, value):
    results = [entry for entry in data if entry.get(key, "").lower() == value.lower()]
    return results

def phonebook(name):
    try:
        with open(f'module_1/Lesson_11/{name}', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('No such file or directory')
        return None
    
    while True:
        print("1. Add new entry")
        print("2. Search by first name")
        print("3. Search by last name")
        print("4. Search by full name")
        print("5. Search by telephone number")
        print("6. Search by city or state")
        print("7. Delete a record by telephone number")
        print("8. Update a record by telephone number")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            entry = {
                "first_name": input("First Name: "),
                "last_name": input("Last Name: "),
                "telephone": input("Phone Number: "),
                "city": input("City or State: "),
            }
            data.append(entry)
        
        elif choice in ["2", "3", "5", "6"]:
            key_map = {"2": "first_name", "3": "last_name", "5": "telephone", "6": "city"}
            key = key_map[choice]
            value = input(f"Enter {key.replace('_', ' ')} to search: ")
            results = search(data, key, value)
            print(f"Search Results: {results}" if results else "No matching records found.")

        elif choice == "4":
            first = input("Enter First Name: ")
            last = input("Enter Last Name: ")
            results = [entry for entry in data if entry.get("first_name") == first and entry.get("last_name") == last]
            print(f"Search Results: {results}" if results else "No matching records found.")

        elif choice == "7":
            phone = input("Enter phone number to delete: ")
            data = [entry for entry in data if entry.get("telephone") != phone]
            
        elif choice == "8":
            phone = input("Enter phone number to update: ")
            for entry in data:
                if entry.get("telephone") == phone:
                    entry["first_name"] = input("New First Name: ")
                    entry["last_name"] = input("New Last Name: ")
                    entry["city"] = input("New City: ")
                    break
            else:
                print("Phone number not found")

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please try again")

    with open(f'module_1/Lesson_11/{name}', "w") as file:
        json.dump(data, file, indent=4)

phonebook("phonebook.json")
