from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
#from sqlalchemy import create_engine, Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String,nullable=False)
    __table_args__ = (
        CheckConstraint('length(phone_number)= 10', name='phone_number'),
    )
                       
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name',)
    def validate_name(self,unique,name):
        if not name:
            raise ValueError("Name not found please entre another name")
        return name
        

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title',)
    def validate_name(self,unique,title):
             
            if 'Won;t Believe,Secret,Top,Guess'not in title:
                 raise ValueError("Name found please entre another name")
            return title
       
            
            



    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
