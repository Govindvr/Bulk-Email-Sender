from flask import Flask

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "app/uploads"

from app import routes