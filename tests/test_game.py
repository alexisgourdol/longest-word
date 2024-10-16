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

    def test_is_word_in_dict_true(self):
            game = Game()
            assert game.is_word_in_dict("tomato") == True
    def test_is_word_in_dict_false(self):
            game = Game()
            assert game.is_word_in_dict("notomato") == False

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


    def test_unknown_word_is_invalid(self):
        """A word that is not in the English dictionary should not be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
