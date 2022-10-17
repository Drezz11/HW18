from flask import json
from flask_restx import Namespace, Resource

from models import GenreSchema, Genre

genre_ns = Namespace()

@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        return GenreSchema(many=True).dumps(Genre.query.all())

@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        result = Genre.query.filter(Genre.id = id).all()
        if len(result):
            return GenreSchema.dump(result), 200
        else:
            return json.dumps({}), 500