patients = []  
queue = []     

def register():
    print("\n-- Patient Registration --")
    name = input("Enter the name: ").strip()
    if not name:
        print("❌ Name cannot be blank.")
        return

    try:
        age = int(input("Enter the age: ").strip())
        if age <= 0:
            print("❌ Age must be positive.")
            return
    except ValueError:
        print("❌ Invalid age. Enter an integer number.")
        return

    phone = input("Enter the phone number: ").strip()
    if not phone:
        print("❌ Phone number cannot be blank.")
        return

    cpf = input("Enter the ID (CPF): ").strip()
    if not cpf:
        print("❌ ID (CPF) cannot be blank.")
        return

    patient = {"name": name, "age": age, "phone": phone, "cpf": cpf}
    patients.append(patient)
    print(f"✅ Patient {name} successfully registered!")

def total_patients():
    return len(patients)

def average_age():
    if not patients:
        return 0
    total = sum(p["age"] for p in patients)
    return total / len(patients)

def youngest_patient():
    if not patients:
        return None
    return min(patients, key=lambda p: p["age"])

def oldest_patient():
    if not patients:
        return None
    return max(patients, key=lambda p: p["age"])

def search_patient():
    name = input("\n🔍 Enter the name of the patient you want to search: ").strip().lower()
    found = [p for p in patients if name in p["name"].lower()]

    if found:
        print(f"\n📁 {len(found)} patient(s) found:")
        for p in found:
            print(f"- {p['name']} | {p['age']} years | {p['phone']} | ID (CPF): {p['cpf']}")
    else:
        print("❌ No patient found with that name.")

def list_patients():
    print("\n📋 List of all registered patients:")
    if not patients:
        print("❌ No patients registered yet.")
        return

    for p in sorted(patients, key=lambda x: x["name"].lower()):
        print(f"- {p['name']} | {p['age']} years | {p['phone']} | ID (CPF): {p['cpf']}")

def statistics():
    print("\n📊 Statistics:")
    if not patients:
        print("❌ No patients registered.")
        return

    print("Total number of patients:", total_patients())
    print("Average age:", round(average_age(), 1))

    youngest = youngest_patient()
    oldest = oldest_patient()

    print("Youngest:", f"{youngest['name']} ({youngest['age']} years)")
    print("Oldest:", f"{oldest['name']} ({oldest['age']} years)")



def add_to_queue():
    """Add a registered patient to the service queue."""
    if not patients:
        print("❌ There are no registered patients to add to the queue.")
        return

    print("\n📥 Patients available to add to the queue:")
    for i, p in enumerate(patients, start=1):
        print(f"{i}. {p['name']} | {p['age']} years | {p['phone']} | ID (CPF): {p['cpf']}")

    choice = input("Enter the number of the patient to add to the queue: ").strip()
    try:
        idx = int(choice)
        if idx < 1 or idx > len(patients):
            print("❌ Invalid number.")
            return
    except ValueError:
        print("❌ Please enter a valid integer number.")
        return

    selected = patients[idx - 1]
    queue.append(selected)
    print(f"✅ Patient {selected['name']} added to the queue.")

def attend_next():
    """Attend the first patient in the queue."""
    if not queue:
        print("\n🕒 No patients in the queue.")
        return

    print("\n----------------------------------------")
    print("Service started...")
    first = queue.pop(0)  
    print(f"Attending: {first['name']} | {first['age']} years | "
          f"{first['phone']} | ID (CPF): {first['cpf']}")
    print("----------------------------------------")

def show_queue():
    """Show all patients currently waiting in the queue."""
    print("\n📌 Patients currently in the queue:")
    if not queue:
        print("No patients waiting.")
        return

    for position, p in enumerate(queue, start=1):
        print(f"{position}. {p['name']} | {p['age']} years | "
              f"{p['phone']} | ID (CPF): {p['cpf']}")


def menu():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Register patient")
        print("2. View statistics")
        print("3. Search patient")
        print("4. List all patients")
        print("5. Add patient to service queue")
        print("6. Attend next patient in queue")
        print("7. Show queue")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            statistics()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            list_patients()
        elif choice == "5":
            add_to_queue()
        elif choice == "6":
            attend_next()
        elif choice == "7":
            show_queue()
        elif choice == "8":
            print("🟤 Exiting the system...")
            break
        else:
            print("❌ Invalid option, try again.")


menu()
