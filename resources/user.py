from flask_restful import Resource ,reqparse
from models.user import UserModels
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token ,create_refresh_token,jwt_required,get_jwt
from models.user import UserModels

post_parser = reqparse.RequestParser()    

post_parser.add_argument('name', type=str , required=True ,   help=""  )
post_parser.add_argument('premon', type=str, required=True, help ="this field cannot blank!")
post_parser.add_argument('email', type=str, required=True, help ="this field cannot blank!")
post_parser.add_argument('telephone', type=str, required=True, help ="this field cannot blank!")
post_parser.add_argument('adresse'  , type=str, required=True, help ="this field cannot blank!")
post_parser.add_argument('password', type=str, requires=True,  help ="this field cannot blank!")

put_parser = post_parser.copy() 





class Usercreate(Resource):
   
   def post(self):
      data = post_parser.parse_args()
      if UserModels.find_by_email(data['email']):
         return  {"message" :"ce email existe deja"}

         user = UserModels(**data) 
         user.save()
      return{"message":"felicitation votre compte est cree"},201



class Userapp(Resource): 
         
     @classmethod
     @jwt_required
     def get(cls ,user_idUniq):
         claims = get_jwt()
         if not claims = ['admin']:
            return {'messsage':'seul admin peut avoir ces infos'}, 401
         user = UserModels.find_by_idUniq(idUniq=user_idUniq)
         if not user:
          return {'message':'user not found'},404
         return user.json()
     
     @classmethod     
     @jwt_required
     def delete(cls,user_idUniq):
         claims = get_jwt()
         if not claims = ['admin']:
            return {'messsage':'seul admin peut avoir ces infos'}, 401
         user=UserModels.find_by_idUniq(idUniq=user_idUniq)
         if not user:
           return {'message':'user  not found'},404
           user.delete()
           return{'message':'user delete' },200
      
class Userlogin(Resource):
     #obtenir des donnees de l'analyse
     #trouver l'utilisateur  dans database
     #verifier le mot de pass
     #creer access au token
     #creer refresh token
     # le return
     @classmethod
     def post(cls):
      data = post_parser.parse_args() 
      user = UserModels.find_by_email(email=data['email'])
      if not user:
         return {"message": "Ce compte n'existe pas"}, 404

      if safe_str_cmp(user.password, data['password']): 
         access_token= create_access_token(identity=user.idUniq, fresh=True)
         refresh_token= create_refresh_token(user.idUniq)
         return { 
         'access_token':access_token,
         'refresh_token': refresh_token
         } ,200

      return {'message':'Invalid'},401
    

    
      







         


    
#route

