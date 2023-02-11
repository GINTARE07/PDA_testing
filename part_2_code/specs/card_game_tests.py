import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("spade", 1)
        self.card2 = Card("heart", 8)
        self.cardGame = CardGame(9)

    def test_card_is_ace(self):

        self.assertEqual(1, self.card1.value)

    def test_can_get_highest_card(self):
        self.assertEqual(1, self.card1.value)

    def test_can_get_cards_total(self):
        total = self.cardGame
        self.assertEquals(9, self.cardGame.cardTotal)


if __name__ == '__main__':
    unittest.main()
