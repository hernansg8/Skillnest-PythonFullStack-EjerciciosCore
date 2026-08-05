from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import date

class Viaje:
    DB = "esquema_simulacro"

    def __init__(self, data):
        self.id = data['id']
        self.destino = data['destino']
        self.fecha_inicio = data['fecha_inicio']
        self.fecha_fin = data['fecha_fin']
        self.itinerario = data['itinerario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.organizador_id = data['organizador_id']
        self.organizador_nombre = data['organizador_nombre']

    @classmethod
    def get_all(cls):
        query = "SELECT" \
                " v.id, v.destino, v.fecha_inicio, v.fecha_fin, v.itinerario," \
                " v.organizador_id, v.created_at, v.updated_at, u.nombre organizador_nombre" \
                " FROM viajes v  " \
                " JOIN usuarios u ON u.id = v.organizador_id" \
                " WHERE fecha_inicio >= current_date() ORDER BY fecha_inicio ASC;"
        results = connectToMySQL(cls.DB).query_db(query)
        items = []
        if results:
            for row in results:
                items.append(cls(row))
        return items

    @classmethod
    def save(cls, data):
        query = "INSERT INTO viajes (destino, fecha_inicio, fecha_fin, itinerario, created_at, updated_at, organizador_id) VALUES (%(destino)s, %(fecha_inicio)s, %(fecha_fin)s, %(itinerario)s, NOW(), NOW(), %(organizador)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT v.id, v.destino, v.fecha_inicio, v.fecha_fin, v.itinerario," \
                " v.organizador_id, v.created_at, v.updated_at, u.nombre organizador_nombre" \
                " FROM viajes v" \
                " JOIN usuarios u ON u.id = v.organizador_id WHERE v.id = %(id)s ;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        if not results:
            return None
        else:
            return (cls(results[0]))

    @classmethod
    def update(cls,data):
        query = "UPDATE viajes SET destino=%(destino)s, fecha_inicio=%(fecha_inicio)s, fecha_fin=%(fecha_fin)s, itinerario=%(itinerario)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM viajes WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    #Validar los registros:
    @staticmethod
    def validar_form(data):
        valid = True
        if date.fromisoformat(data['fecha_inicio']) < date.today():
            flash('La fecha de inicio debe ser mayor a la actual.','error')
            valid = False
        if data['fecha_inicio'] > data['fecha_fin']:
            flash('La fecha de termino tiene que ser mayor a la fecha de inicio.', 'error')
            valid = False
        if len(data['itinerario'])>40:
            flash('El itinerario no puede superar los 40 carácteres.','error')
            valid = False
        return valid