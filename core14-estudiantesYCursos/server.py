#########################
#|  PYTHON FULL STACK   |
#| CORE 14              |
#| Hernán Soto          |
#########################

from flask_app import app
from flask_app.controllers import curso_controller
from flask_app.controllers import estudiante_controller

if __name__ == "__main__":
    app.run(debug=True)
