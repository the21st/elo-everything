# ELO Everything

ELO Everything is a website that pulls popular and recognizable concepts from Wikipedia and lets visitors vote on which one they like better. It then calculates scores for each concept using the ELO rating system and displays them on a leaderboard.

## Setup

1. Clone the repository:

```
git clone https://github.com/yourusername/elo_everything.git
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Set up the database:

```
python models/concept.py
python models/user.py
python models/vote.py
```

## Running the Application

1. Start the application:

```
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`.

## Testing

To run the tests:

```
python tests/test_wiki_scraper.py
python tests/test_elo_calculator.py
python tests/test_app.py
```

## Deployment

The application is deployed using fly.io. To deploy:

1. Install the fly CLI:

```
curl -L https://fly.io/install.sh | sh
```

2. Login to fly:

```
flyctl auth login
```

3. Deploy the application:

```
flyctl deploy
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)