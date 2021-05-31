from db import db
from  ma import ma
from uuid import uuid4

def generate_uuid():
    return str(uuid4())[:7]

class UserModels (db.Model):
    __tablename__= 'users'
    #colonne
    id = db.Column('user_id',db.Integer, primary_key = True)
    idUniq = db.column(db.String(10),unique=True, nullable=False)
    name = db.column(db.Sting(80))
    premon = db.column(db.String(80), nullable=False)
    email = db.column(db.String(100),unique=True, nullable=False)
    telephone = db.colum(db.String(100))
    adresse = db.colum(db.String(100),unique=True, nullable=False)
    password = db.colum(db.String(100),unique=True, nullable=False)
     
    #constructeur
    def __init__ (self,name,prenom,email,telephone,adresse,password) :
        self.name = name
        self.idUniq = f"cl_{generate_uuid()}"
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
        self.adresse = adresse 
        self.password = password

    @classmethod
    def json(self):
        return {'name': self.name, 'price': self.email, 'telephone': self.telephone  , 'adresse':self.adresse  }
  
    @classmethod 
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id).first()
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_by_idUniq(cls, idUniq):
        return cls.query.filter_by(idUniq=idUniq).first()

    def save(self):
       db.session.add(self)
       db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    


    