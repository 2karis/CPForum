from flask import Flask

import sqlalchemy

from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Text


class Post(Base):
	__tablename__ = 'Post'

	id = Column(Integer, primary_key=True)
	location = Column(String)
	number = Column(Integer)
	description = Column(Text)
	image = Column(String)

	def __repr__(self):
		return "<Post(location='%s', number='%s', description='%s', image='%s')>" % (
	                     self.location, self.number, self.description, self.image)


app = Flask(__name__)

@app.route('/')
def hello_world():

	post = Post(location='atlanta', number=5, description=' there are several people there and one sick person', image='image.jpeg')

	return post.image


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/upload')
def show_upload():
    # show the post with the given id, the id is an integer
    return 'upload'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)


