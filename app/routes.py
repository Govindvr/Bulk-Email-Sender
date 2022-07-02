from email import message
import os
from app import app
from flask import redirect, render_template, request, flash
from werkzeug.utils import secure_filename
from app.send import send

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'csv'}

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            msg = request.form.get("message")
            print(msg)
            send(filename)
            return "success"
        else:
            flash("Wrong file type")
            return render_template("pg.html")

    return render_template("pg.html")