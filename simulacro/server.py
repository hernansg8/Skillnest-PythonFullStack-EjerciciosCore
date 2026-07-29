from flask_app import app
from flask_app.controllers import usuario_controller
from flask_app.controllers import viajes_controller
from flask_app.controllers import viajeros_controller

if __name__ == "__main__":
    app.run(debug=True)
