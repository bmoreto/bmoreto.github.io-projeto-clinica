from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder=".")

patients = []
current_queue = []


def register_patient(name, age_str, phone, cpf):
    name = name.strip()
    phone = phone.strip()
    cpf = cpf.strip()

    if not name:
        return False, "Name cannot be blank."
    if not phone:
        return False, "Phone number cannot be blank."
    if not cpf:
        return False, "ID (CPF) cannot be blank."

    try:
        age = int(age_str.strip())
        if age <= 0:
            return False, "Age must be positive."
    except ValueError:
        return False, "Invalid age. Enter an integer number."

    patient = {"name": name, "age": age, "phone": phone, "cpf": cpf}
    patients.append(patient)
    return True, f"Patient {name} successfully registered!"


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


def search_patient(query):
    if not query:
        return []
    query = query.strip().lower()
    return [p for p in patients if query in p["name"].lower()]


def list_patients():
    return patients


def statistics():
    if not patients:
        return None
    return {
        "total": total_patients(),
        "avg_age": round(average_age(), 1),
        "youngest": youngest_patient(),
        "oldest": oldest_patient(),
    }


def add_to_queue(index_str):
    if not patients:
        return False, "There are no registered patients."

    try:
        idx = int(index_str)
    except ValueError:
        return False, "Invalid patient number."

    if idx < 0 or idx >= len(patients):
        return False, "Patient not found."

    patient = patients[idx]
    current_queue.append(patient)
    return True, f"Patient {patient['name']} added to the current queue."


def attend_next():
    if not current_queue:
        return False, "No patients in the current queue."

    patient = current_queue.pop(0)

    msg = (
        f"Attending: {patient['name']} | {patient['age']} years | "
        f"{patient['phone']} | ID (CPF): {patient['cpf']}"
    )
    return True, msg


@app.route("/", methods=["GET", "POST"])
def index():
    message = request.args.get("message", "")
    error = ""
    search_results = None
    search_query = ""

    if request.method == "POST":
        action = request.form.get("action")

        if action == "register":
            name = request.form.get("name", "")
            age = request.form.get("age", "")
            phone = request.form.get("phone", "")
            cpf = request.form.get("cpf", "")
            ok, msg = register_patient(name, age, phone, cpf)
            if ok:
                return redirect(url_for("index", message=msg))
            else:
                error = msg

        elif action == "add_to_queue":
            patient_index = request.form.get("patient_index", "")
            ok, msg = add_to_queue(patient_index)
            if ok:
                return redirect(url_for("index", message=msg))
            else:
                error = msg

        elif action == "attend_next":
            ok, msg = attend_next()
            if ok:
                return redirect(url_for("index", message=msg))
            else:
                error = msg

        elif action == "search":
            search_query = request.form.get("search_name", "")
            search_results = search_patient(search_query)

    stats = statistics()
    ordered_patients = list_patients()

    return render_template(
        "index.html",
        patients=ordered_patients,
        current_queue=current_queue,
        message=message,
        error=error,
        stats=stats,
        search_results=search_results,
        search_query=search_query,
    )


if __name__ == "__main__":
    app.run(debug=True)
