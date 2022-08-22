from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:antoine@localhost/11AUG(audio)'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DATABASE_URL= $(heroku config:get postgresql+psycopg2://postgres:antoine@localhost/11AUG(audio) -a mini-soundcloud-clone) your_process

class Uploading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uploads = db.Column(db.String(100), unique=True)

    def __init__(self, uploads):
        self.uploads = uploads


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Tracks')
def Tracks():
    return render_template('Tracks.html')


@app.route('/file_uploaded', methods=['GET','POST'])
def file_uploaded():
    if request.method=='POST':
        files = request.files['files']
        file_path = f'static/uploads/{files.filename}'
        files.save(file_path)
        input = Uploading(uploads = f'static/uploads/{secure_filename(files.filename)}')
        db.session.add(input)
        db.session.commit()
    return render_template('file_uploaded.html',file=files.filename)
   
    # if request.method == 'POST':
    #    files=request.files['file']
    #    file_path = f'static/databases/{secure_filename(files.filename)}'
    #    files.save(file_path)
    #    input = dataUploads(upload = f'static/databases/{secure_filename(files.filename)}')
    #    db.session.add(input)
    #    db.session.commit()
    #    return render_template('file_uploaded.html',file=files.filename)



if __name__ == "__main__":
    app.run()
