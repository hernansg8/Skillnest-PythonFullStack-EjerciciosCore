# ==========================================
# __init__.py
# Inicializa la aplicación Flask
# ==========================================

from flask import Flask

app = Flask(__name__)
app.secret_key = "simulacropythonmysql"
