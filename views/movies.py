from flask import request, json
from flask_restx import Namespace, Resource

from models import Movie, MovieSchema
from setup_db import db

movie_ns = Namespace()


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        query = Movie.query()
        if director_id:
            query = query.filter(Movie.director_id = director_id)
        if genre_id:
            query = query.filter(Movie.genre_id = genre_id)
        if year:
            query = query.filter(Movie.year = year)
        return MovieSchema(many=True).dump(query.all()), 200

    def post(self):
        data = request.json
        try:
            db.session.add(Movie(**data))
            db.session.commit()
            return "Добавлено!", 200
        except Exception as e:
            print(e)
            db.session.rollback()
            return "Запись недобавлена", 500

@movie_ns.route('/<int:mid>')
class MovieViews(Resource):
    def get(self, mid):
        result = Movie.query(Movie).filter(Movie.id == id).all()
        if len(result):
            return MovieSchema().dump(result), 200
        else:
            return json.dumps({}), 200

    def put(self, mid):
        data = request.json
        try:
            result = Movie.query.filter(Movie.id = id).one()
            result.title = data.get('title')
            db.session.add(result)
            db.session.commit()
            return "Обновлено", 200
        except Exception as e:
            print(e)
            db.session.rollback()
            return "Не обновлено", 500

    def delete(self, mid):
        try:
            result = Movie.query.filter(Movie.id == id).one()
            db.session.delete(result)
            db.session.commit()
            return "Удалилось", 200
        except Exception:
            db.session.rollback()
            return "Не удалилось", 500





