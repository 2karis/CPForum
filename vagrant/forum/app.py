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

	posts = [  # fake array of posts
        { 
            'location': 'five points', 
            'number': '6',
            'description': 'a group of elderly people are hanging around five points',
            'image':'DSC_0100.jpg',
        },
         { 
            'location': 'five points', 
            'number': '6',
            'description': 'a group of elderly people are hanging around five points',
            'image':'17378825_BG1.jpg',
        },
         { 
            'location': 'five points', 
            'number': '6',
            'description': 'a group of elderly people are hanging around five points',
            'image':'16029849_BG1.jpg',
        },
         { 
            'location': 'five points', 
            'number': '6',
            'description': 'a group of elderly people are hanging around five points',
            'image':'image.png',
        }
    ]
	return render_template('homepage.html',  posts=posts)

@app.route('/contact')
def contactPage():
	return render_template('contact.html')

@app.route('/about')
def aboutPage():
	return render_template('about.html')

@app.route('/pic')
def pic():

	post = {'location': 'five points', 
            'number': '6',
            'description': 'a group of elderly people are hanging around five points',
            'image':'DSC_0100.jpg' }
	return render_template('pic.html', post=post)

#@app.route('/upload', methods=['GET', 'POST'])
#def upload():
	#if request.method == 'POST':
		#f = request.files['the_file']
		#f.save('/var/www/uploads/uploaded_file.txt')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)