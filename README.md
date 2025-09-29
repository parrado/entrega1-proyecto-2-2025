<h1 align="center">
Entrega: Servidor del Sistema de Teleconsulta (RA 1, RA 2, RA 3 y RA 4) <br />
 </h1>
 <p align="center">
Alexander López-Parrado, PhD. <br />
Programación, II-2025 <br />
GDSPROC <br />
Uniquindío <br />
</p>

Con esta práctica se iniciará el desarrollo del código fuente en Python del proyecto del espacio académico. En este caso, y de acuerdo a la arquitectura mostrada en la siguiente figura, se construirá el código del lado del servidor para la gestión de usuarios y de consultas médicas.

<p align="center">
<img  src="Programación-II-2025.png" width="800" >
</p>
En ese sentido, esta parte del proyecto contempla la creación y prueba de las funciones construidas en la práctica de laboratorio anterior. 

## Código base suministrado

Se suministra el código base del servidor en el archivo [project_server.py](project_server.py) el cual contiene toda la funcionalidad para que éste opere dentro de una red de área local o en el mismo equipo de prueba. **En este archivo se debe realizar el llamada de las funciones construidas por su equpipo de trabajo** de acuerdo a los comentarios incluidos. **La correcta integración de estas funciones y su correcto funcionamiento determina la evaluación del lado del servidor del proyecto**.

El servidor debe permitir el registro de usuarios con un nombre, número de identificación, contraseña y rol, y una vez un usuario esté registrado podrá:

* Iniciar sesión usando el número de identificación y la contraseña.
* Solicitar una consulta con un médico.
* Listar los médicos disponibles

Se debe incluir en el archivo [project_server.py](project_server.py) las funciones creadas en el lab1 y una nueva función que permite listar los médicos disponibles.

De otro lado, se suministran los archivos [project_client.py](project_client.py) y [test_project_client.py](test_project_client.py). En este caso,  [project_client.py](project_client.py) implementa la funcionalidad básica de los usuarios para la conexión con el servidor por lo que **no debe ser modificado bajo ninguna circunstancia**. De otro lado,  [test_project_client.py](test_project_client.py) es un archivo de prueba que se suministra para verificar el correcto funcionamiento del servidor y que puede ser modificado a gusto de los miembros del equipo. Para que [project_client.py](project_client.py) pueda funcionar correctamente se debe instalar el módulo de Python requests ejecutando el siguiente comando en una terminal:

``` pip install requests ```


## ¿Cómo realizar las pruebas?

Para la realización de las pruebas debe ejecutar primero el programa [project_server.py](project_server.py), la recomendación es verificar el correcto funcionamiento de las funciones, una a la vez. Posteriormente se puede ejecutar el programa [test_project_client.py](test_project_client.py), en caso de que se creen ventanas emergentes de Windows solicitando permisos, por favor otorgarlos ya que los programas hacen uso de los servicios de red. 

Tenga en cuenta que es posible que [project_server.py](project_server.py) y[test_project_client.py](test_project_client.py) se ejecuten en computadores diferentes siempre y cuando los equipos se encuentren conectados a la misma red LAN cableada o inalámbrica. En ese caso basta con consultar la dirección IP del computador que está ejecutando  [project_server.py](project_server.py) mediante el comando ipconfig como se muestra en la siguiente figura.


<p align="center">
<img  src="Captura de pantalla (2).png" width="800" >
</p>

La IP encontrada debe sustituir "localhost" en la línea 6 de [test_project_client.py](https://github.com/parrado/lab2/blob/c80a0f73b9324b082ebea63a3377358d36a4c8d8/test_trivia_client.py#L6#L6)

# Entrega del laboratorio

El laboratorio debe ser presentado mediante:

1. Repositorio en GitHub.
2. Informe de laboratorio.

El informe de laboratorio y el enlace al repositorio de GitHub deben ser compartidos en el enlace dispuesto para tal fin en la plataforma Google Classroom.
