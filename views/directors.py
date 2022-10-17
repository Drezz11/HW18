from flask import request, json
from flask_restx import Namespace, Resource

from models import Director, DirectorSchema

director_ns = Namespace()

@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        return DirectorSchema(many=True).dumps(Director.query.all())

@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        result = Director.query.filter(Director.id = id).all()
        if len(result):
            return DirectorSchema().dump(result), 200
        else:
            return json.dumps({}), 200