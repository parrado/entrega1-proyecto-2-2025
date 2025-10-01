from project_client import Client

# Intenta registrar un usuario
name="sebastian"
password="00000"
role="patient"
id=12345
url="http://localhost:80"

project_client=Client(url)

print(project_client.registerUser(name,id,password,role))


# Inicia sesión con usuario
print(project_client.openSession(id,password))

# Obtiene la lista de médicos
print(project_client.getDoctorsList(id))


doctorid=54321
date="2025-07-01"
time="10:00"


# Solicita una cita con un médico
print(project_client.addAppointment(doctorid,id,date,time))



# Cierra sesión con usuario
print(project_client.closeSession(id))
