from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager 
#JWT est un gestionnaires
from resources.even import Event, Eventcreate
from resources.user import Usercreate,Userapp,Userlogin
from resources.org import  Orgapp,Orglogin,Orgcreate
from resources.admin import Admincreate,Adminapp,Adminlogin

from models.user import UserModels
from models.org import OrganModels
from models.admin import AdminModels

# de module importons les  class disponibles   
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/event hub'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key ='hermann'
api = Api(app)

jwt = JWTManager(app)
 #connecter application
 #lorsque vous obtenez des donnez utilisateur flask_jwt_extended se en mesure
 # de determiner que vous avez reçu la demande et sera en mesure 
 # fournir les donnees sur utilisateur  qui a fait la demande

@jwt.additional_claims_loader
def add_claims_to_access_token(identity):
    # identity look at for idUniq
    user = UserModels.find_by_idUniq(idUniq=identity)
    org = OrganModels.find_by_idUniq(idUniq=identity)
    admin = AdminModels.find_by_idUniq(idUniq=identity)

    if user:
        return {'client': True, 'org': False, 'admin': False}
    elif org:
        return {'client': False, 'org': True, 'admin': False}
    elif admin:
        return {'client': False, 'org': False, 'admin': True}
    else:
        return {'client': False, 'org': False, 'admin': False}



@jwt.expired_token_loader


api.add_resource()
api.add_resource(Userapp,'/usercompte/<int:id>')
api.add_resource(Usercreate, '/public')
api.add_resource(Eventcreate, '/events')
api.add_resource(Event, '/event/<int:id>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all(app=app)

    app.run(debug=True)
