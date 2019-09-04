import unittest
from models import movie

Movie = movie.Movie


class MovieTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_movie = Movie(1234,'Python must be crazy','A thrilling new python series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

    def test_init(self):
        '''
        Test to check whether object is intantiated properly
        '''
        self.assertEqual(self.new_movie.id,1234)
        self.assertEqual(self.new_movie.title,'Python must be crazy')
        self.assertEqual(self.new_movie.overview,'A thrilling new python series')
        self.assertEqual(self.new_movie.poster,'https://image.tmdb.org/t/p/w500/https://image.tmdb.org/t/p/w500/khsjha27hbs')
        self.assertEqual(self.new_movie.vote_average,8.5)
        self.assertEqual(self.new_movie.vote_count,129993)

if __name__ == "__main__":
    unittest.main()