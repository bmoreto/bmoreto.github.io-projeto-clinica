patients = []  

def register():
    while True:
        print("\n-- Patient Registration --")
        name = input("Enter the name (or 'exit' to finish): ").strip()

        if name.lower() == "exit":
            print("🟤 Ending registration...")
            break

        if not name:
            print("❌ Name cannot be blank.")
            continue

        try:
            age = int(input("Enter the age: ").strip())
            if age <= 0:
                print("❌ Age must be positive.")
                continue
        except ValueError:
            print("❌ Invalid age. Please enter a number.")
            continue

        phone = input("Enter the phone number: ").strip()
        if not phone:
            print("❌ Phone number cannot be blank.")
            continue

        patient = {"name": name, "age": age, "phone": phone}
        patients.append(patient)
        print(f"✅ Patient {name} successfully registered!")

register()