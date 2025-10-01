# Instalar el módulo requests haciendo desde una terminal: pip install requests
import requests
import socket



# Función para registrar usuario
def addAppointment(url,id,doctorid,date,time):    
    response=requests.post(url+'/addappointment',data=f'id={id}&doctorid={doctorid}&date={date}&time={time}')
    return response.content.decode('utf-8')


# Función para registrar usuario
def registerUser(url,name,id,role,password):    
    response=requests.post(url+'/register',data=f'name={name}&id={id}&role={role}&password={password}')
    return response.content.decode('utf-8')

# Funciónn para abrir una sesión
def openSession(url,id,password):
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)    
    response=requests.put(url+'/login',data=f'id={id}&password={password}&ip={IPAddr}')
    return response.content.decode('utf-8')

# Función para cerrar una sesión
def closeSession(url,id):    
    response=requests.put(url+'/logout',data=f'id={id}')
    return response.content.decode('utf-8')




# Función para obtener la lista de médicos
def getDoctorsList(url,id):    
    response=requests.get(url+'/listdoctors',data=f'id={id}')
    return response.content.decode('utf-8')





