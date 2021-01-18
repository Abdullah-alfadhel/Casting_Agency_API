import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, Movies, Actors, setup_db, setup_migrations
from .auth.auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  setup_db(app)
  setup_migrations(app)

  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers',
                            "Content-Tpe,Authorization,true")
      response.headers.add('Access-Control-Allow-Methods',
                            'GET,PUT,POST,PATCH,DELETE,OPTIONS')
      return response
  
  @app.route('/movies', methods=['GET'])
  @requires_auth('get:drinks-detail')
  def get_movies():
      movies = Movies.query.all()
      print(movies, 'this is it')
      data = [movie.format() for movie in movies]

      return jsonify({
          "success": True,
          "movies": data
          }), 200
  
  @app.route('/movies/<int:movie_id>', methods=['GET'])
  @requires_auth('get:drinks-detail')
  def get_movie(movie_id):
      movie = Movies.query.filter_by(id=movie_id).all()
      print(movie, 'this is it')

      if not movie:
        abort(404)

      return jsonify({
          "success": True,
          "movie": movie[0].format()
          }), 200
  
  @app.route('/actors', methods=['GET'])
  @requires_auth('get:drinks-detail')
  def get_actors():
      actors = Actors.query.all()
      print(actors, 'this is it')
      
      

      data = [actor.format() for actor in actors]
      return jsonify({
          "success": True,
          "actors": data
          }), 200
  
  @app.route('/actors/<int:actor_id>', methods=['GET'])
  @requires_auth('get:drinks-detail')
  def get_actor(actor_id):
      actor = Actors.query.filter_by(id=actor_id).all()
      print(actor, 'this is it')

      if not actor:
        abort(404)

      return jsonify({
          "success": True,
          "actor": actor[0].format()
          }), 200
  
  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('get:drinks-detail')
  def delete_movie(movie_id):
      movie = Movies.query.filter(Movies.id == movie_id).one_or_none()

      if not movie:
          abort(404)

      try:
          movie.delete()
      except Exception:
          abort(400)

      return jsonify({
          'success': True,
          'delete': movie_id
          }), 200
  
  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('get:drinks-detail')
  def delete_actor(actor_id):
      actor = Actors.query.filter(Actors.id == actor_id).one_or_none()

      if not actor:
          abort(404)

      try:
          actor.delete()
      except Exception:
          abort(400)

      return jsonify({
          'success': True,
          'delete': actor_id
          }), 200
  
  @app.route('/movies', methods=['POST'])
  @requires_auth('get:drinks-detail')
  def create_movie():
      req = request.get_json()

      try:
          movie = Movies(title = req['title'], release_date = req['release_date'])
          movie.insert()

      except Exception:
          abort(400)

      return jsonify({
          'success': True,
          'movie': movie.format()
          }), 200
  
  @app.route('/actors', methods=['POST'])
  @requires_auth('get:drinks-detail')
  def create_actor():
      req = request.get_json()

      try:
          actor = Actors(name=req['name'], age= req['age'], gender=req['gender'])
          actor.insert()

      except Exception:
          abort(400)

      return jsonify({
          'success': True,
          'actor': actor.format()
          }), 200
  
  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('get:drinks-detail')
  def patch_movie(movie_id):
      req = request.get_json()
      movie = Movies.query.filter(Movies.id == movie_id).one_or_none()

      if not movie:
          abort(404)

      try:
          title = req.get('title')
          release_date = req.get('release_date')
          if title:
              movie.title = title

          if release_date:
              movie.release_date = release_date

          movie.update()
      except Exception:
          abort(400)

      return jsonify({
          'success': True,
          'movie': movie.format()
          }), 200
  
  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('get:drinks-detail')
  def patch_actor(actor_id):
      req = request.get_json()
      actor = Actors.query.filter(Actors.id == actor_id).one_or_none()

      if not actor:
          abort(404)

      try:
          name = req.get('name')
          age = req.get('age')
          gender = req.get('gender')
          if name:
              actor.name = name

          if age:
              actor.age = age

          if gender:
              actor.gender = gender

          actor.update()
      except Exception:
          abort(400)

      return jsonify({
          'success': True,
          'actor': actor.format()
          }), 200
  
  @app.errorhandler(AuthError)
  def auth_error(error):
      return jsonify({
          "success": False,
          "error": error.status_code,
          "message": error.error['description']
      }), error.status_code

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request error'
        }), 400

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({
          'success': False,
          'error': 404,
          'message': 'Resource not found'
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
          'success': False,
          'error': 500,
          'message': 'Internal error, please try again.'
        }), 500

    @app.errorhandler(422)
    def uncrossable_entity(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Uncrossable entity'
        }), 422

  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)