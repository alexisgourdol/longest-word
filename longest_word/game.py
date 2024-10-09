# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

from random import choice
from string import ascii_uppercase
from collections import Counter
import requests

class Game:
    def __init__(self):
        """Attribute a random grid to size 9"""
        self.grid = [choice(ascii_uppercase) for _ in range(9)]

    def is_word_in_dict(self, word: str) -> bool:
        url = "https://dictionary.lewagon.com/"
        response = requests.get(f"{url}{word}")
        if response.status_code == 200:
            return response.json()["found"]
        return False

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        # print(f"{sum(Counter(word).values()) <= sum(Counter(self.grid).values())=}")
        # print(f"{set(Counter(word)).issubset(set(Counter(self.grid)))=}")
        if word == "":
            return False

        is_subset = set(Counter(word)).issubset(set(Counter(self.grid)))
        is_length_ok = sum(Counter(word).values()) <= sum(Counter(self.grid).values())
        is_in_dict = self.is_word_in_dict(word)
        return is_subset and is_length_ok and is_in_dict


if __name__ == "__main__":
    g = Game()
    TEST_GRID = "KWEUEAKRZ"
    g.grid = list(TEST_GRID)
    g.is_valid("EUREKA")
