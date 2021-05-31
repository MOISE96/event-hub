from flask_restful import Resource ,reqparse
from models.admin import AdminModels
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token ,create_refresh_token,jwt_required,get_jwt


post_parser = reqparse.RequestParser()    

post_parser.add_argument('name', type=str , required=True ,   help=""  )
post_parser.add_argument('password', type=str, requires=True,  help ="this field cannot blank!")

put_parser = post_parser.copy() 





class Admincreate(Resource):
   
   def post(self):
      data = post_parser.parse_args()
      if AdminModels.find_by_email(data['email']):
         return  {"message" :"ce email existe deja"}

         Admin = AdminModels(**data) 
         Admin.save()
      return{"message":"felicitation votre compte est cree"},201



class Adminapp(Resource):
         
     @classmethod
     def get(cls ,admin_idUniq):
       admin =AdminModels.find_by_idUniq(idUniq=admin_idUniq)
       if not admin: 
        return {'message':'admin not found'},404
        return admin.json()
     
     @classmethod     
   
     def delete(cls,admin_idUniq):
      admin = AdminModels.find_by_idUniq(idUniq=admin_idUniq)
      if not admin:
           return {'message':'admin  not found'},404
           org.delete()
           return{'message':'admin delete' },200
      
class Adminlogin(Resource):
     #obtenir des donnees de l'analyse
     #trouver l'utilisateur  dans database
     #verifier le mot de pass
     #creer access au token
     #creer refresh token
     # le return
     def post(cls):
      data = post_parser.parse_args() 
      admin = AdminModels.find_by_email(email=data['email'])
      if not admin:
         return {"message": "Ce compte n'existe pas"}, 404

      if safe_str_cmp(admin.password, data['password']): 
         access_token= create_access_token(identity=admin.idUniq, fresh=True)
         refresh_token= create_refresh_token(admin.idUniq)
         return { 
         'access_token':access_token,
         'refresh_token':refresh_token
         } ,200

      return {'message':'Invalid'},401
    
      