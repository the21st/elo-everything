from flask_wtf import FlaskForm
from wtforms import SubmitField

class VoteForm(FlaskForm):
    vote_button1 = SubmitField('Vote for Concept 1')
    vote_button2 = SubmitField('Vote for Concept 2')