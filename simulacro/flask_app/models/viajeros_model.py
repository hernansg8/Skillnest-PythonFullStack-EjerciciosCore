from flask_app.config.mysqlconnection import connectToMySQL

class Viajero:
    DB = "esquema_simulacro"
    
    def __init__(self, data):
        self.viaje_id = data['viaje_id']
        self.usuario_id = data['usuario_id']

    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM viajeros WHERE viaje_id=%(id)s"
        results = connectToMySQL(cls.DB).query_db(query,data)
        viajeros = []
        for row in results:
            viajeros.append(cls(row))
        return viajeros

    @classmethod
    def save(cls, data):
        query = "INSERT INTO viajeros (viaje_id, usuario_id) VALUES (%(viaje_id)s, %(usuario_id)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM viajeros WHERE viaje_id = %(viaje_id)s AND usuario_id = %(usuario_id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)