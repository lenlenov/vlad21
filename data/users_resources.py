from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify
from . import db_session
from data.users import User
from flask import Flask


app = Flask(__name__)
api = Api(app)


def abort_if_users_not_found(users_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(users_id)
    if not users:
        abort(404, message=f"Users {users_id} not found")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        db_sess = db_session.create_session()
        users = db_sess.query(User).get(users_id)
        return jsonify({'users': users.to_dict(
            only=('id', 'team_leader', 'user', 'work_size',
                  'collaborators', 'start_date',
                  'end_date', 'is_finished'))})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        db_sess = db_session.create_session()
        users = db_sess.query(User).get(users_id)
        db_sess.delete(users)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'team_leader', 'user', 'work_size',
                  'collaborators', 'start_date',
                  'end_date', 'is_finished')) for item in users]})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        parser.add_argument('team_leader', required=True)
        parser.add_argument('user', required=True, type=bool)
        parser.add_argument('work_size', required=True, type=bool)
        parser.add_argument('collaborators', required=True, type=int)
        parser.add_argument('start_date', required=True, type=int)
        parser.add_argument('end_date', required=True, type=int)
        parser.add_argument('is_finished', required=True, type=int)
        args = parser.parse_args()
        db_sess = db_session.create_session()
        users = User(
            id=args['id'],
            team_leade=args['team_leade'],
            user=args['user'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date = args['start_date'],
            end_date = args['end_date'],
            is_finished = args['is_finished']
        )
        db_sess.add(users)
        db_sess.commit()
        return jsonify({'success': 'OK'})
