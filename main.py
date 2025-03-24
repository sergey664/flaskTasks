from flask import Flask, redirect, render_template
from flask_login import LoginManager, login_user, login_required, logout_user
from sql.data import db_session
from sql.data.login_form import LoginForm
from sql.data.register import RegisterForm
from sql.data.add_job import Job
from sql.data.__all_models import users, jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(users.User, user_id)


@app.route('/')
def index():
    session = db_session.create_session()
    jobs_list = session.query(jobs.Jobs).all()
    jobs_data = []

    for job in jobs_list:
        team_leader = session.query(users.User).filter((users.User.id == job.team_leader)).first()
        jobs_data.append({
            "id": job.id,
            "title": job.job,
            "team_leader": f"{team_leader.name} {team_leader.surname}" if team_leader else "Unknown",
            "duration": f"{job.work_size} hours",
            "collaborators": job.collaborators,
            "is_finished": "Yes" if job.is_finished else "No"
        })

    return render_template("index.html", file='style.css', jobs=jobs_data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(users.User).filter((users.User.email == form.email.data)).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        if form.password.data == form.password_repeat.data:
            new_user = users.User(
                email=form.email.data,
                surname=form.surname.data,
                name=form.name.data,
                age=form.age.data,
                position=form.position.data,
                speciality=form.speciality.data,
                address=form.address.data
            )
            new_user.set_password(form.password.data)
            session.add(new_user)
            session.commit()
            return redirect('/')

    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


# --> Обработчик addjob <--
@app.route('/addjob', methods=['GET', 'POST'])
def add_job():
    form = Job()
    session = db_session.create_session()
    if form.validate_on_submit():
        new_job = jobs.Jobs(
            job=form.job.data,
            team_leader=form.team_leader.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            is_finished=form.is_finished.data
        )
        session.add(new_job)
        session.commit()
        return redirect('/')

    return render_template('addjob.html', form=form)
# --> Обработчик addjob <--


def main():
    db_session.global_init("sql/db/mars.db")
    app.run()


if __name__ == '__main__':
    main()
