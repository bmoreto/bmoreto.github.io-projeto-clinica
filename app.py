patients = [] 

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

    patient = {"name": name, "age": age, "phone": phone}
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
            print(f"- {p['name']} | {p['age']} years | {p['phone']}")
    else:
        print("❌ No patient found with that name.")

def list_patients():
    print("\n📋 List of all registered patients:")
    if not patients:
        print("❌ No patients registered yet.")
        return

    for p in sorted(patients, key=lambda x: x["name"].lower()):
        print(f"- {p['name']} | {p['age']} years | {p['phone']}")

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


def menu():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Register patient")
        print("2. View statistics")
        print("3. Search patient")
        print("4. List all patients")
        print("5. Exit")

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
            print("🟤 Exiting the system...")
            break
        else:
            print("❌ Invalid option, try again.")


# ===== Run program =====
menu()