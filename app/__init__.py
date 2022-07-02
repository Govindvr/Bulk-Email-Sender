from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'l\xf0\xdb3\xdbB\\T$\x86\x83\xef\x1f\x05/a\xaa\xf28\xc8\x01oN1' 
app.config['UPLOAD_FOLDER'] = "app/uploads"

from app import routes