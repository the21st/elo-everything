1. Dependencies: These are shared across all Python files and are listed in "requirements.txt". They include Flask, SQLAlchemy, BeautifulSoup, requests, etc.

2. Database Models: "concept.py", "user.py", and "vote.py" define the data schemas for the concepts, users, and votes respectively. These are used across the application.

3. Wiki Scraper: The function "scrape_wiki" in "wiki_scraper.py" is used in "app.py" to pull data from Wikipedia.

4. ELO Calculator: The function "calculate_elo" in "elo_calculator.py" is used in "app.py" to calculate ELO scores.

5. DOM Elements: The "index.html" and "leaderboard.html" files contain DOM elements with ids such as "concept1", "concept2", "vote-button", "leaderboard-table" which are used in "main.js".

6. CSS Styles: The "main.css" file contains styles that are used across the HTML templates.

7. JavaScript Functions: The "main.js" file contains functions like "vote", "loadConcepts", "updateLeaderboard" that are used across the HTML templates.

8. Dockerfile: This file is used to build a Docker image for the application, which is used in the deployment pipeline.

9. fly.toml: This file contains configuration for the fly.io deployment pipeline.

10. Procfile: This file is used by Heroku or other platforms to start the application.

11. .gitignore: This file lists files and directories that should be ignored by Git, shared across the project.

12. README.md: This file contains instructions for setting up and running the application, which are relevant across the project.