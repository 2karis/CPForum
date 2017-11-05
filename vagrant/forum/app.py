from flask import Flask
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Homeless
app = Flask(__name__)


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

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		f = request.files['the_file']
		f.save('/var/www/uploads/uploaded_file.txt')



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)