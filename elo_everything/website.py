```python
from flask import Flask, render_template, request, redirect, url_for, flash
from .models import db, Concept, Score
from .views import index, leaderboard, vote
from .utils import get_random_concepts
from .elo_calculator import calculate_elo
from .wikipedia_scraper import scrape_wikipedia

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'your-secret-key'

db.init_app(app)

app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/leaderboard', 'leaderboard', leaderboard, methods=['GET'])
app.add_url_rule('/vote', 'vote', vote, methods=['POST'])

@app.before_first_request
def setup():
    db.create_all()
    initial_concepts = ['Water', 'Common Cold', 'Queen Elizabeth II']
    for concept in initial_concepts:
        data = scrape_wikipedia(concept)
        new_concept = Concept(name=concept, description=data['description'], image_url=data['image_url'])
        db.session.add(new_concept)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
```