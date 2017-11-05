from flask import Flask
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Homeless
from datetime import datetime
import os
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

engine = create_engine('sqlite:///lesshome.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/homepage')
def homePage():

	posts = session.query(Homeless).all()
	return render_template('homepage.html',  posts=posts)

@app.route('/contact')
def contactPage():
	return render_template('contact.html')

@app.route('/about')
def aboutPage():
	return render_template('about.html')

@app.route('/pic/<int:post_id>')
def pic(post_id):

	posts =  session.query(Homeless).filter_by(id=post_id).first() 

	return render_template('pic.html', post=posts), 'Post %d' % post_id

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload():
 	if request.method == 'POST':
 		file = request.files['file']

 		if file and allowed_file(file.filename):
 			filename = secure_filename(file.filename)
 			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
 			return redirect('/')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)