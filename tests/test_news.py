import unittest
from app.models import Source,Articles


class SourceTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the News class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.new_sources = Source(1234, 'Amazing news', 'Thrilling news', 'https://abcnews.go.com', 'Technology',
                             'UnitedStates', 'English')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources, Source))

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.new_articles=Articles('nice','forr','what',"ooh",'woow','kiki')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles, Articles)) 

      


if __name__ == '__main__':
    unittest.main()