# users.py
from datetime import date
from datetime import datetime


# This function must return the list of doctors, user with user_id must be a patient and have an open session
def doctorsList(user_id):
    # Include the code to return the list of doctors

    listOfDoctors=[] 

    
    return listOfDoctors

def openSession(user_id, password, ip):
    # Include here the call of function you coded to open session. Store ip string in your field for open session.
    # Your function should return a message string.
    msg=f"Message from openSession function for user {user_id} from ip {ip}"
    
    return msg
    
def closeSession(user_id):
    # Include here the call of function you coded to close session. Store an empty string in your field for open session.
    # Your function should return a message string.
    msg=f"Message from closeSession function for user {user_id}"
    
    return msg

  

def registerUser(name, user_id, role, password):
    # Include here the call of function you coded to register users.
    # Your function should return a message string.
    msg=f"Message from register user function for user {user_id}"
    
    return msg

def addAppointment(user_id, doctor_id, date, time):
    # Include here the call of function you coded to add appointments.
    # Your function should return a message string.
    msg=f"Message from addAppointment function for user {user_id} with doctor {doctor_id} on {date} at {time}"
    
    return msg

""" 
This function returns IP of doctor to the client.
Following conditions must be met before returning IP:
* Pacient must have a session opened
* Doctor must have a session opened
* Pacient must have an scheduled appointment with doctor
* Request time and date must fit in current time and date



"""

def getDoctorIP(user_id):

    myDate = date.today()
    myTime= datetime.now().time()
    msg=f"Message from getDoctorIP function for user {user_id}, {myDate},{myTime}"   

    return msg
