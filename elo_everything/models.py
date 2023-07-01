```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Concept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id'), nullable=False)
    elo_score = db.Column(db.Float, default=1000.0)
    concept = db.relationship('Concept', backref=db.backref('scores', lazy=True))
```