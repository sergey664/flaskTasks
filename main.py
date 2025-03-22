from flask import Flask, render_template
from sql.data.jobs import Jobs
from sql.data.users import User
from sql.data.db_session import create_session, global_init

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    session = create_session()
    jobs_list = session.query(Jobs).all()
    jobs_data = []

    for job in jobs_list:
        team_leader = session.query(User).filter((User.id == job.team_leader)).first()
        jobs_data.append({
            "id": job.id,
            "title": job.job,
            "team_leader": f"{team_leader.name} {team_leader.surname}" if team_leader else "Unknown",
            "duration": f"{job.work_size} hours",
            "collaborators": job.collaborators,
            "is_finished": "Yes" if job.is_finished else "No"
        })

    return render_template("addjob.html", file='style.css', jobs=jobs_data)


def main():
    global_init("sql/db/mars.db")
    app.run()


if __name__ == '__main__':
    main()
