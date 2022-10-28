import json
from flask import Flask, jsonify, request

from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

conexion = MySQL(app)

@app.route('/people', methods=['GET'])
def showPeople():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT identificacion, nombre, apellidos, edad FROM personas"
        cursor.execute(sql)
        datos = cursor.fetchall()

        arrayPeople = []

        for fila in datos:
            p = {'identificacion' : fila[0] , 'nombre' : fila[1], 'apellidos' : fila[2], 'edad' : fila[3]} 
            arrayPeople.append(p)
        return jsonify({'people' : arrayPeople, 'message' : "Personas registradas"})

    except Exception as ex:
        return jsonify({'message' : "Algo salio mal"})

@app.route('/people/<identificacion>', methods=['GET'])
def searchPeople(identificacion):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT identificacion, nombre, apellidos, edad FROM personas WHERE identificacion = '{0}'".format(identificacion) 
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            p = {'identificacion' : datos[0] , 'nombre' : datos[1], 'apellidos' : datos[2], 'edad' : datos[3]} 
            return jsonify({'people' : p, 'message' : "Persona encontrada"})
        else:
            return jsonify({'message' : "persona no registrada"})

    except Exception as ex:
        return jsonify({'message' : "Algo salio mal"})        


@app.route('/people', methods=['POST'])
def addPeople():
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO personas VALUES ('{0}','{1}','{2}',{3})".format(request.json['identificacion'], request.json['nombre'], request.json['apellidos'], request.json['edad']) 
        cursor.execute(sql)        
        conexion.connection.commit()

        return jsonify({'message' : "persona registrada"})
    except Exception as ex:
        return jsonify({'message' : "Algo salio mal"})


@app.route('/people/<identificacion>', methods=['DELETE'])
def deletePeople(identificacion):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM personas WHERE identificacion = '{0}'".format(identificacion) 
        print(sql)
        cursor.execute(sql)        
        conexion.connection.commit()

        return jsonify({'message' : "persona eliminada"})
    except Exception as ex:
        return jsonify({'message' : "Algo salio mal"})


@app.route('/people/<identificacion>', methods=['PUT'])
def updatePeople(identificacion):
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql = "UPDATE personas SET nombre = '{0}', apellidos = '{1}', edad = {2} WHERE identificacion = '{3}'".format(request.json['nombre'], request.json['apellidos'], request.json['edad'], identificacion) 
        print(sql)
        cursor.execute(sql)        
        conexion.connection.commit()

        return jsonify({'message' : "persona actualizada"})
    except Exception as ex:
        return jsonify({'message' : "Algo salio mal"})


def showError(error):
    return "<h3>Pagina no encontrada por el momento</h3>"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,showError)
    app.run()