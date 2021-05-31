from db import db

# creation de la table events
class EventModel(db.Model):
    __tablename__ = 'events'
    # columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    date_pub = db.Column(db.String(200))

    #constructor
    def __init__(self, name, description,date_pub ):
        self.name = name
        self.description = description
        self.date_pub = date_pub
    
    @classmethod
    #select * FROM events where name = name
    #fitrage par nom de chaque evenemnt
    def find_by_name(cls,name):
        return EventModel.query.filter_by(name=name).first()


    #enregiter le model Event dans la base de donne
    def save(self):
        #permet d'ajouter des objet et commit pour envoie
        db.session.add(self)
        db.session.commit()
    
    
     # mise jour = delete= supprimer l'objet
     # commit pour envoyer
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
    

