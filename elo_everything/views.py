```python
from flask import render_template, redirect, url_for, flash
from elo_everything import app, db
from elo_everything.models import Concept, Score
from elo_everything.forms import VoteForm
from elo_everything.utils import get_random_concepts
from elo_everything.elo_calculator import calculate_elo

@app.route('/')
def index():
    concept1, concept2 = get_random_concepts()
    form = VoteForm()
    return render_template('index.html', title='ELO Everything', concept1=concept1, concept2=concept2, form=form)

@app.route('/vote', methods=['POST'])
def vote():
    form = VoteForm()
    if form.validate_on_submit():
        winner = Concept.query.get(form.winner.data)
        loser = Concept.query.get(form.loser.data)
        winner_score = Score.query.filter_by(concept_id=winner.id).first()
        loser_score = Score.query.filter_by(concept_id=loser.id).first()
        new_winner_score, new_loser_score = calculate_elo(winner_score.score, loser_score.score)
        winner_score.score = new_winner_score
        loser_score.score = new_loser_score
        db.session.commit()
        flash('vote_success', 'success')
    else:
        flash('vote_error', 'error')
    return redirect(url_for('index'))

@app.route('/leaderboard')
def leaderboard():
    scores = Score.query.order_by(Score.score.desc()).all()
    return render_template('leaderboard.html', title='Leaderboard', scores=scores)
```