from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_login import UserMixin


class Job(FlaskForm, UserMixin):
    job = StringField('Работа', validators=[DataRequired()])
    team_leader = StringField('Лидер', validators=[DataRequired()])
    work_size = StringField('Размер работы', validators=[DataRequired()])
    collaborators = StringField('Рабочие', validators=[DataRequired()])
    start_date = DateField('Начало', validators=[DataRequired()])
    end_date = DateField('Конец', validators=[DataRequired()])
    is_finished = BooleanField('Готово')
    submit = SubmitField('Добавить')
