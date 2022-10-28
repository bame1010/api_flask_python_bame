****************************************************************************
                                                                           *
       USO DE LA API DE PERSONAS USANDO PYTHON, FLASK, MYSQL               *
                                                                           *
****************************************************************************

1- API DE LISTAR Personas
****************************************************************************
Por medio de esta API vamos a poder listar y visualizar en formato JSON    *
las personas que se encuentran registradas en la base de datos MYSQL, para *
su uso vamos a usar POSTMAN o cURL así:                                    *
                                                                           *
METHOD: GET                                                                *
   URL: http://localhost:5000/people                                       *
                                                                           *
****************************************************************************


2- API FILTRAR Personas
****************************************************************************
Por medio de esta API vamos a poder consultar y visualizar en formato JSON *
por medio de la cedula a cualquier persona que se encuentra registrada en  *
la base de datos MYSQL, para su uso vamos a usar POSTMAN o cURL así:       *
                                                                           *
METHOD: GET                                                                *
   URL: http://localhost:5000/people/1085316160                            *
                                                                           *
****************************************************************************


3- API CREAR UNA Personas
****************************************************************************
Por medio de esta API vamos a crear a una persona y registrarlar en la     *
la base de datos y para ello vamos a usar el metodo POST y vamos a enviar  *
en formato JSON nuestros datos simulando la petición por medio de          *
POSTMAN o cURL así:                                                        *
                                                                           *
METHOD: POST                                                               *
   URL: http://localhost:5000/people
  JSON: {
            "identificacion" : "64565",
            "nombre" : "Andrea Stefania",
            "apellidos" : "Salas Urbina",
            "edad" : 31
        }                                                                  *
                                                                           *
****************************************************************************


4- API MODIFICAR Persona
****************************************************************************
Por medio de esta API vamos a modificar una persona que ya se encuentra    *
registrarda en la base de datos y para ello vamos a usar el metodo PUT y   *
vamos a enviar en formato JSON nuestros datos simulando la petición por    *
medio de POSTMAN o cURL así:                                               *
                                                                           *
METHOD: PUT                                                                *
   URL: http://localhost:5000/people/64565
  JSON: {
            "nombre" : "Carolina Andrea",
            "apellidos" : "Ortega Riascos",
            "edad" : 25
        }                                                                  *
                                                                           *
****************************************************************************


5- API ELIMINAR Personas
****************************************************************************
Por medio de esta API vamos a poder eliminar por medio del metodo DEL a    *
cualquier persona que se encuentra registrada en usando su numero de CC    *
la base de datos MYSQL, para su uso vamos a usar POSTMAN o cURL así:       *
                                                                           *
METHOD: DEL                                                                *
   URL: http://localhost:5000/people/1085316160                            *
                                                                           *
****************************************************************************


****************************************************************************
                                                                           *
                         BASE DE DATOS MYSQL                               *
                                                                           *
****************************************************************************

NOMBRE DB: prueba 
    TABLE: personas
   FILEDS:
+----------------+--------------+------+-----+---------+-------+
| Field          | Type         | Null | Key | Default | Extra |
+----------------+--------------+------+-----+---------+-------+
| identificacion | varchar(50)  | YES  |     | NULL    |       |
| nombre         | varchar(100) | YES  |     | NULL    |       |
| apellidos      | varchar(100) | YES  |     | NULL    |       |
| edad           | bigint       | YES  |     | NULL    |       |
+----------------+--------------+------+-----+---------+-------+