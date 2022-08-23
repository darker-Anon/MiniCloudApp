from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nacbvyxvgzspie:214ef7f9e792ec1379deafcbe36ea4844279922c9219575dfbc253f156e6c52d@ec2-34-199-68-114.compute-1.amazonaws.com:5432/d63ie289q6nurf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
