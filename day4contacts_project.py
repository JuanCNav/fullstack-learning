contacts = []

while True:
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts.append({"name": name, "phone": phone})
        print("Contact added!")

    elif choice == "2":
        if not contacts:
            print("No contacts yet.")
        else:
            for c in contacts:
                print(f"{c['name']} → {c['phone']}")

    elif choice == "3":
        search = input("Search name: ").lower()
        found = False
        for c in contacts:
            if c["name"].lower() == search:
                print(f"Found: {c['name']} → {c['phone']}")
                found = True
                break
        if not found:
            print("Not found.")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")