import unittest
from unittest.mock import patch
from elo_everything.wikipedia_scraper import scrape_wikipedia

class TestWikipediaScraper(unittest.TestCase):

    @patch('elo_everything.wikipedia_scraper.requests.get')
    def test_scrape_wikipedia(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'Queen Elizabeth II'

        result = scrape_wikipedia('Queen_Elizabeth_II')
        self.assertEqual(result, 'Queen Elizabeth II')

        mock_get.assert_called_once_with('https://en.wikipedia.org/wiki/Queen_Elizabeth_II')

    @patch('elo_everything.wikipedia_scraper.requests.get')
    def test_scrape_wikipedia_failure(self, mock_get):
        mock_get.return_value.status_code = 404

        result = scrape_wikipedia('Non_Existent_Page')
        self.assertIsNone(result)

        mock_get.assert_called_once_with('https://en.wikipedia.org/wiki/Non_Existent_Page')

if __name__ == '__main__':
    unittest.main()