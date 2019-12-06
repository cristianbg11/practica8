
from zeep import Client

url = "http://localhost:7777/ws/AcademicoWebService?wsdl"
client = Client(url)

# Listar estudiantes
estudiante = client.service.getAllEstudiante()
print estudiante

#Consultar asignatura
asignatura = client.service.getAsignatura(2)
print asignatura

# Consultar profesor
print client.service.getProfesor('123123').nombre
