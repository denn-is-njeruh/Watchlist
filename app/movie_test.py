import unittest
from models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
        '''
        Test Class to test the behaviour of the Movie class
        '''

        def setUp(self):
            '''
            Set up method that run before every test.
            '''
            self.new_movie =  Movie(1234,'Python Must be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

        def test_instance(self):
            self.assertTrue(isinstance(self.new_movie,Movie))

        
        def test_init(self):
            '''
            test_init test case to test if the object is instantiated properly.
            '''
            self.assertEqual(self.new_movie.id,1234)
            self.assertEqual(self.new_movie.title,"Python Must be Crazy")
            self.assertEqual(self.new_movie.overview,"A thrilling new Python Series")
            self.assertEqual(self.new_movie.poster,"https://image.tmdb.org/t/p/w500/khsjha27hbs")
            self.assertEqual(self.new_movie.vote_average,8.5)
            self.assertEqual(self.new_movie.vote_count,129993)


if __name__ == '__main__':
    unittest.main()