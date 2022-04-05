from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job_title = StringField('Title job', validators=[DataRequired()])
    team_leader_id = IntegerField('id leader')
    work_size = IntegerField('Work size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_fin = BooleanField("Is job finished?")
    submit = SubmitField('Применить')