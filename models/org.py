from models.user import generate_uuid
from db import db
from  ma import ma


class OrganModels(db.Model):

    __tablename__= 'organisateur'
    #colonne
    id = db.Column('user_id',db.Integer, primary_key = True)
    idUniq = db.column(db.String(10),unique=True, nullable=False)
    name = db.column(db.Sting(80))
    premon = db.column(db.String(80),unique=True, nullable=False)
    email = db.column(db.String(100),unique=True, nullable=False)
    telephone = db.colum(db.String(100))
    adresse = db.colum(db.String(100),unique=True, nullable=False)
    password = db.colum(db.String(100),unique=True, nullable=False)

    def __init__ (self,name,prenom,email,telephone,adresse,password):
        self.idUniq = f"or_{generate_uuid()}"
        self.name = name
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
        self.adresse = adresse 
        self.password = password

    def save (self):
       db.session.add(self)
       db.session.commit()

    @classmethod
    def json(self):
        return {'name': self.name, 'email': self.email, 'telephone': self.telephone  , 'adresse':self.adresse  }
  

    @classmethod 
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
  
    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id).first()
    
    @classmethod
    def find_by_idUniq(cls, idUniq):
        return cls.query.filter_by(idUniq=idUniq).first()


    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
