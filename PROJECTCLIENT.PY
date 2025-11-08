from project_client import Client

url = "http://localhost:80"
client = Client(url)

#Registrar doctores
print("=== REGISTRANDO DOCTORES ===")
print(client.registerUser("Dr. Juan", "54321", "doctor", "1234"))
print(client.registerUser("Dra. María", "98765", "doctor", "abcd"))

#Registrar paciente
print("\n=== REGISTRANDO PACIENTE ===")
print(client.registerUser("Felipe", "12345", "patient", "0000"))

#Iniciar sesión
print("\n=== INICIANDO SESIÓN DEL PACIENTE ===")
print(client.openSession("12345", "0000"))

#Listar doctores
print("\n=== LISTA DE MÉDICOS DISPONIBLES ===")
print(client.getDoctorsList("12345"))

#Solicitar cita
print("\n=== SOLICITANDO CITA ===")
print(client.addAppointment("12345", "54321", "2025-11-10", "09:30"))

#Intentar cita repetida
print("\n=== PROBANDO CITA DUPLICADA ===")
print(client.addAppointment("12345", "54321", "2025-11-10", "09:30"))

#Cerrar sesión
print("\n=== CERRANDO SESIÓN ===")
print(client.closeSession("12345"))

#Intentar listar médicos sin sesión
print("\n=== PROBANDO LISTA SIN SESIÓN ===")
print(client.getDoctorsList("12345"))


