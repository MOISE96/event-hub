from flask_restful import Resource ,reqparse
from models.org import OrganModels
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token ,create_refresh_token,jwt_required,get_jwt


post_parser = reqparse.RequestParser()    

post_parser.add_argument('name', type=str , required=True ,   help=""  )
post_parser.add_argument('premon', type=str, required=True, help ="this field cannot blank!")
post_parser.add_argument('email', type=str, required=True, help ="this field cannot blank!")
post_parser.add_argument('telephone', type=str, required=True, help ="this field cannot blank!")
post_parser.add_argument('adresse'  , type=str, required=True, help ="this field cannot blank!")
post_parser.add_argument('password', type=str, requires=True,  help ="this field cannot blank!")

put_parser = post_parser.copy() 





class Orgcreate(Resource):
   
   def post(self):
      data = post_parser.parse_args()
      if OrganModels.find_by_email(data['email']):
         return  {"message" :"ce email existe deja"}

         Org = OrganModels(**data) 
         Org.save()
      return{"message":"felicitation votre compte est cree"},201



class Orgapp(Resource):
         
     @classmethod
     def get(cls ,org_idUniq):
       org = OrganModels.find_by_idUniq(idUniq=org_idUniq)
       if not org: 
        return {'message':'orgnisateur not found'},404
        return org.json()
     
     @classmethod     
   
     def delete(cls,org_idUniq):
      org = OrganModels.find_by_idUniq(idUniq=org_idUniq)
      if not org:
           return {'message':'orgnisateur  not found'},404
           org.delete()
           return{'message':'orgnisateur delete' },200
      
class Orglogin(Resource):
     #obtenir des donnees de l'analyse
     #trouver l'utilisateur  dans database
     #verifier le mot de pass
     #creer access au token
     #creer refresh token
     # le return
     def post(cls):
      data = post_parser.parse_args() 
      org = OrganModels.find_by_email(email=data['email'])
      if not org:
         return {"message": "Ce compte n'existe pas"}, 404

      if safe_str_cmp(org.password, data['password']): 
         access_token= create_access_token(identity=org.idUniq, fresh=True)
         refresh_token= create_refresh_token(org.idUniq)
         return { 
         'access_token':access_token,
         'refresh_token': refresh_token
         } ,200

      return {'message':'Invalid'},401
    
      







         


    
#route

