import unittest
from elo_everything.utils.wiki_scraper import scrape_wiki

class TestWikiScraper(unittest.TestCase):

    def test_scrape_wiki(self):
        # Test scraping a known page
        concept, image = scrape_wiki("Water")
        self.assertEqual(concept, "Water")
        self.assertTrue(image.startswith("https://"))

        # Test scraping a non-existent page
        with self.assertRaises(Exception):
            scrape_wiki("NonExistentPage")

if __name__ == '__main__':
    unittest.main()