from longest_word.game import Game
from string import ascii_uppercase

# tests/test_game.py
class TestGame:
    def test_game_initialization(self):
        # setup
        game = Game()

        # exercise
        grid = game.grid

        # verify
        assert isinstance(grid, list)
        assert len(grid) == 9

        for letter in grid:
            assert letter in  ascii_uppercase
        # teardown

    def test_empty_word_is_invalid(self):
            game = Game()
            assert game.is_valid("") == False

    def test_word_is_too_long(self):
            game = Game()
            test_grid = 'KWEUEAKRZ'
            test_word = 'BLABLABLIBLUEBLA'
            # exercice
            game.grid = list(test_grid) # Force the grid to a test case
            assert game.is_valid(test_word) == False
            assert game.grid == list(test_grid) # Make sure the grid remained untouched

    def test_word_is_valid(self):
        game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'
        # exercice
        game.grid = list(test_grid) # Force the grid to a test case
        assert game.is_valid(test_word) == True
        assert game.grid == list(test_grid) # Make sure the grid remained untouched


    def test_word_invalid(self):
            game = Game()
            test_grid = 'KWEUEAKRZ'
            test_word = 'SANDWICH'
            # exercice
            game.grid = list(test_grid) # Force the grid to a test case
            assert game.is_valid(test_word) == False
            assert game.grid == list(test_grid) # Make sure the grid remained untouched
