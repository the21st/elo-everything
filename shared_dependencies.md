1. Exported Variables:
   - `app` (Flask application instance) in `website.py`
   - `db` (Database instance) in `models.py`

2. Data Schemas:
   - `Concept` (Schema for the concepts like "Water", "Common Cold", etc.) in `models.py`
   - `Score` (Schema for the ELO scores of each concept) in `models.py`

3. ID Names of DOM Elements:
   - `concept1` and `concept2` (The two concepts to be compared) in `index.html`
   - `vote-button1` and `vote-button2` (Buttons to vote for a concept) in `index.html`
   - `leaderboard-table` (Table to display the leaderboard) in `leaderboard.html`

4. Message Names:
   - `vote_success` (Message displayed when a vote is successfully cast) in `views.py`
   - `vote_error` (Message displayed when there is an error in casting a vote) in `views.py`

5. Function Names:
   - `get_random_concepts` (Function to get two random concepts) in `utils.py`
   - `calculate_elo` (Function to calculate ELO scores) in `elo_calculator.py`
   - `scrape_wikipedia` (Function to scrape data from Wikipedia) in `wikipedia_scraper.py`
   - `index` (Function to render the main page) in `views.py`
   - `leaderboard` (Function to render the leaderboard page) in `views.py`
   - `vote` (Function to handle voting) in `views.py`

6. Test Function Names:
   - `test_get_random_concepts` in `test_website.py`
   - `test_calculate_elo` in `test_elo_calculator.py`
   - `test_scrape_wikipedia` in `test_wikipedia_scraper.py`