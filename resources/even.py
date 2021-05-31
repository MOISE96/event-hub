from typing import Optional
from flask_jwt_extended.jwt_manager import JWTManager

from flask_jwt_extended.utils import get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from models.event import EventModel 
from flask_restful import reqparse
from flask_jwt_extended import get_jwt_identity,get_jwt

post_parser = reqparse.RequestParser()
post_parser.add_argument ('name' , type=str , required=True, help ="Th blank!")
post_parser.add_argument ('description' , type=str, required=True, help ="Thise lank!")
post_parser.add_argument ('date_pub' , type=str, required=True, help ="Thise lank!")

put_parser = post_parser.copy() 
put_parser.remove_argument('mdp')

class Event(Resource):
     
    @classmethod 
    def get(cls, id):
        event = EventModel('eggge', 'gfgfgf', 'ddfdfdd')
        event.save()
        return {'message' : event.name}

    def delete(self, id):
        # /event/<int:id>
         event = Event.find_by_id(id)
         if event:
             event.delete_from_db()
         return {'message':' Event delete'}
    
    def put (self,name):
        data = Event.parser.parse_args()
        data = EventModel (name )


class Eventcreate(Resource):
     @classmethod
     @jwt_required
     def post(cls):
        claims = get_jwt
        if not claims = ['admin']:
            return {'messsage':'seul organisateur peut avoir ces infos'}, 401

         # post_parser est une variable
         # parse_args renvoie certaine données des paramètres précisés
        args = post_parser.parse_args(strict=True)
        print(args)
        event = EventModel(args.name, args.description, args.date_pub)
        event.save()
        return {'msg': 'yes'}, 201

   
        @jwt_required(Optional=True)
        class Eventlist(Resource):
    # /events
         def get(self):
             user_idUniq = get_jwt_identify()
             event = [event.json() for event in EventModel.fin.all()]

             if user_idUniq:
                  
              return { 'event':events},200
              return( 
                 'events':[event['name'] for event in events],
                   'message': 'vos donnees sont incorrect'
                  ),200