#########################
#|  PYTHON FULL STACK   |
#| Core 16              |
#| Hernán Soto          |
#########################

from flask_app import app
from flask_app.controllers import usuario_controller
from flask_app.controllers import evento_controller

if __name__ == "__main__":
    app.run(debug=True)
