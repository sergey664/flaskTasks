import flask
from sql.data import db_session
from sql.data.jobs import Jobs

blueprint = flask.Blueprint("jobs_api", __name__, template_folder="templates", url_prefix="/api")


@blueprint.route("/jobs")
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return flask.jsonify(
        {
            'jobs':
                [item.to_dict(only=("id",
                                    "job",
                                    "work_size",
                                    "collaborators",
                                    "start_date",
                                    "end_date",
                                    "is_finished",
                                    "team_leader"))
                 for item in jobs]
        }
    )


@blueprint.route("/job/<int:job_id>")
def get_job(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return flask.make_response(flask.jsonify({"error": "Not found"}), 404)
    return {
        "jobs": job.to_dict(only=("id",
                                  "job",
                                  "work_size",
                                  "collaborators",
                                  "start_date",
                                  "end_date",
                                  "is_finished",
                                  "team_leader"))
    }
