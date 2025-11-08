# users.py
import json
import os

# Archivos de almacenamiento
USERS_FILE = "users_data.json"
APPOINTMENTS_FILE = "appointments_data.json"

# --- Funciones auxiliares para manejo de archivos ---
def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# --- Cargar datos iniciales ---
users_db = load_data(USERS_FILE)
appointments_db = load_data(APPOINTMENTS_FILE)

# --- Función para registrar un usuario ---
def registerUser(name, user_id, role, password):
    global users_db
    # Validar duplicados
    for u in users_db:
        if u["id"] == user_id:
            return f"User {user_id} already exists."
    
    new_user = {
        "name": name,
        "id": user_id,
        "role": role,
        "password": password,
        "session_ip": ""
    }
    users_db.append(new_user)
    save_data(USERS_FILE, users_db)
    return f"User {user_id} registered successfully as {role}."


# --- Función para abrir sesión ---
def openSession(user_id, password, ip):
    global users_db
    for u in users_db:
        if u["id"] == user_id:
            if u["password"] == password:
                u["session_ip"] = ip
                save_data(USERS_FILE, users_db)
                return f"Session opened for user {user_id} from IP {ip}."
            else:
                return f"Invalid password for user {user_id}."
    return f"User {user_id} not found."


# --- Función para cerrar sesión ---
def closeSession(user_id):
    global users_db
    for u in users_db:
        if u["id"] == user_id:
            if u["session_ip"] != "":
                u["session_ip"] = ""
                save_data(USERS_FILE, users_db)
                return f"Session closed for user {user_id}."
            else:
                return f"User {user_id} has no active session."
    return f"User {user_id} not found."


# --- Función para listar médicos ---
def doctorsList(user_id):
    global users_db
    for u in users_db:
        if u["id"] == user_id:
            if u["role"] != "patient":
                return ["Access denied: only patients can list doctors."]
            if u["session_ip"] == "":
                return ["You must log in first."]
            
            doctors = [x for x in users_db if x["role"] == "doctor"]
            return [{"id": d["id"], "name": d["name"]} for d in doctors]

    return ["User not found."]


# --- Función para agendar una cita ---
def addAppointment(user_id, doctor_id, date, time):
    global users_db, appointments_db

    patient = next((u for u in users_db if u["id"] == user_id), None)
    doctor = next((u for u in users_db if u["id"] == doctor_id), None)

    if not patient:
        return f"Patient {user_id} not found."
    if not doctor:
        return f"Doctor {doctor_id} not found."
    if patient["session_ip"] == "":
        return f"Patient {user_id} must log in first."
    if doctor["role"] != "doctor":
        return f"User {doctor_id} is not a doctor."

    # Validar duplicados (mismo doctor, fecha y hora)
    for a in appointments_db:
        if a["doctor"] == doctor_id and a["date"] == date and a["time"] == time:
            return f"Doctor {doctor_id} is not available at {date} {time}."

    new_appointment = {
        "patient": user_id,
        "doctor": doctor_id,
        "date": date,
        "time": time
    }
    appointments_db.append(new_appointment)
    save_data(APPOINTMENTS_FILE, appointments_db)
    return f"Appointment created with doctor {doctor_id} on {date} at {time}."

