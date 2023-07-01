```python
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.concept import Concept
from models.user import User
from models.vote import Vote
from utils.wiki_scraper import scrape_wiki
from utils.elo_calculator import calculate_elo
import random

app = Flask(__name__)
engine = create_engine('sqlite:///elo_everything.db')
Session = sessionmaker(bind=engine)

@app.route('/')
def index():
    session = Session()
    concepts = session.query(Concept).all()
    if len(concepts) < 2:
        concepts_data = scrape_wiki()
        for concept_data in concepts_data:
            concept = Concept(**concept_data)
            session.add(concept)
        session.commit()
        concepts = session.query(Concept).all()
    concept1, concept2 = random.sample(concepts, 2)
    return render_template('index.html', concept1=concept1, concept2=concept2)

@app.route('/vote', methods=['POST'])
def vote():
    session = Session()
    concept_id = request.form.get('concept_id')
    concept = session.query(Concept).get(concept_id)
    concept.elo_score = calculate_elo(concept.elo_score)
    session.commit()
    return redirect(url_for('index'))

@app.route('/leaderboard')
def leaderboard():
    session = Session()
    concepts = session.query(Concept).order_by(Concept.elo_score.desc()).all()
    return render_template('leaderboard.html', concepts=concepts)

if __name__ == '__main__':
    app.run(debug=True)
```