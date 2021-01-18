import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, Movies, Actors

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)

  @app.route('/movies', methods=['GET'])
  def get_movies():
      movies = Movies.query.all()
      print(movies, 'this is it')

      return jsonify({
          "success": True,
          "movies": movies.format()
          }), 200
  
  @app.route('/movies/<int:movie_id>', methods=['GET'])
  def get_movie(movie_id):
      movie = Movies.query.filter_by(id=movie_id).all()
      print(movie, 'this is it')

      return jsonify({
          "success": True,
          "movie": movie.format()
          }), 200
  
  @app.route('/actors', methods=['GET'])
  def get_actors():
      actors = Actors.query.all()
      print(actors, 'this is it')

      return jsonify({
          "success": True,
          "actors": actors.format()
          }), 200
  
  @app.route('/actors/<int:actor_id>', methods=['GET'])
  def get_actor(actor_id):
      actor = Actors.query.filter_by(id=actor_id).all()
      print(actor, 'this is it')

      return jsonify({
          "success": True,
          "actor": actor.format()
          }), 200
  
  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
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
  def create_movie(data):
      req = request.get_json()

      try:
          movie = Movies()
          movie.title = req['title']
          movie.release_date = req['release_date']
          movie.insert()

      except Exception:
          abort(400)

      return jsonify({
          'success': True,
          'movie': movie.format()
          }), 200
  
  @app.route('/actors', methods=['POST'])
  def create_actor(data):
      req = request.get_json()

      try:
          actor = Actors()
          actor.name = req['name']
          actor.age = req['age']
          actor.gender = req['gender']
          actor.insert()

      except Exception:
          abort(400)

      return jsonify({
          'success': True,
          'actor': actor.format()
          }), 200
  
  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
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


  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)