from models.user import generate_uuid
from db import db
from  ma import ma


class AdminModels (db.Model):
    __tablename__= 'admin'
    #colonne
    id = db.Column('user_id',db.Integer, primary_key = True)
    idUniq = db.column(db.String(10),unique=True, nullable=False)
    name = db.column(db.Sting(80))
    password = db.colum(db.String(100),unique=True, nullable=False)
     
    #constructeur

    def __init__ (self,name,prenom,email,telephone,adresse,password):
        self.idUniq = f"ad_{generate_uuid()}"
        self.name = name
        self.password = password

    def save (self):
       db.session.add(self)
       db.session.commit()

    @classmethod
    def json(self):
        return {'name': self.name,   'password':self.password  }
  
    @classmethod
    def find_by_idUniq(cls, idUniq):
        return cls.query.filter_by(idUniq=idUniq).first()

    @classmethod 
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
  
    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id).first()


    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
