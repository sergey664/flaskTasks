import flask
from sql.data import db_session
from sql.data.users import User

blueprint = flask.Blueprint("users", __name__, template_folder="templates", url_prefix="/api")


@blueprint.route("/users")
def get_users():
    session = db_session.create_session()
    users = session.query(User).all()
    return flask.jsonify(
        {
            'users':
                [item.to_dict(only=("id",
                                    "surname",
                                    "name",
                                    "position",
                                    "speciality",
                                    "address",
                                    "email"))
                 for item in users]
        }
    )


@blueprint.route("/user/<int:job_id>")
def get_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return flask.make_response(flask.jsonify({"error": "Not found"}), 404)
    return {
        "user": user.to_dict(only=("id",
                                   "surname",
                                   "name",
                                   "position",
                                   "speciality",
                                   "address",
                                   "email"))
    }
