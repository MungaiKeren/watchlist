import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Review class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.all_reviews = Review(1234,'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs')

    def test_instance(self):
        self.assertTrue(isinstance(self.all_reviews,Review))
