from flask import Flask, render_template, request

# diz ao Flask que os templates (HTML) estão na pasta raiz "."
app = Flask(__name__, template_folder=".")

patients = []   # lista de pacientes cadastrados
queue = []      # fila de atendimento (usa os mesmos pacientes)


# ===== FUNÇÕES DE NEGÓCIO =====

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


def add_to_queue(index_str):
    if not patients:
        return False, "There are no registered patients."

    try:
        idx = int(index_str)
    except ValueError:
        return False, "Invalid patient number."

    # usamos index da lista (0, 1, 2...)
    if idx < 0 or idx >= len(patients):
        return False, "Patient not found."

    patient = patients[idx]
    queue.append(patient)
    return True, f"Patient {patient['name']} added to the queue."


def attend_next():
    if not queue:
        return False, "No patients in the queue."

    patient = queue.pop(0)
    msg = (
        f"Attending: {patient['name']} | {patient['age']} years | "
        f"{patient['phone']} | ID (CPF): {patient['cpf']}"
    )
    return True, msg


# ===== ROTA PRINCIPAL (HTML) =====

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    error = ""

    if request.method == "POST":
        action = request.form.get("action")

        # 1) Cadastrar paciente
        if action == "register":
            name = request.form.get("name", "")
            age = request.form.get("age", "")
            phone = request.form.get("phone", "")
            cpf = request.form.get("cpf", "")

            ok, msg = register_patient(name, age, phone, cpf)
            if ok:
                message = msg
            else:
                error = msg

        # 2) Adicionar paciente na fila
        elif action == "add_to_queue":
            patient_index = request.form.get("patient_index", "")
            ok, msg = add_to_queue(patient_index)
            if ok:
                message = msg
            else:
                error = msg

        # 3) Atender próximo paciente
        elif action == "attend_next":
            ok, msg = attend_next()
            if ok:
                message = msg
            else:
                error = msg

    return render_template(
        "index.html",
        patients=patients,
        queue=queue,
        message=message,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
