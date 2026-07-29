from flask_app.config.mysqlconnection import connectToMySQL

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

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM viajes WHERE fecha_inicio > now() ORDER BY fecha_inicio ASC;"
        results = connectToMySQL(cls.DB).query_db(query)
        viajes = []
        for row in results:
            viajes.append(cls(row))
        return viajes

    @classmethod
    def save(cls, data):
        query = "INSERT INTO viajes (destino, fecha_inicio, fecha_fin, itinerario, created_at, updated_at, organizador_id) VALUES (%(destino)s, %(fecha_inicio)s, %(fecha_fin)s, %(itinerario)s, NOW(), NOW(), %(organizador)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM viajes WHERE id = %(id)s ;"
        resultados = connectToMySQL(cls.DB).query_db(query,data)
        for row in resultados:
            return cls(row)

    @classmethod
    def update(cls,data):
        query = "UPDATE viajes SET destino=%(destino)s, fecha_inicio=%(fecha_inicio)s, fecha_fin=%(fecha_fin)s, itinerario=%(itinerario)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM viajes WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)