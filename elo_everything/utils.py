```python
import random
from elo_everything.models import Concept

def get_random_concepts():
    all_concepts = Concept.query.all()
    if len(all_concepts) < 2:
        return None, None
    concept1, concept2 = random.sample(all_concepts, 2)
    return concept1, concept2
```