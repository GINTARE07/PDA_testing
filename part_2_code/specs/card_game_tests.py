import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = Card("Spades", 1)
        self.card1 = Card("Diamonds", 8)
        self.card2 = Card("Hearts", 2)
        cards = []
        self.cardGame = CardGame(cards)

    def test_card_is_ace(self):
        self.assertEqual(True, self.cardGame.check_for_ace(self.card))

    def test_card_is_not_ace(self):
        self.assertEqual(False, self.cardGame.check_for_ace(self.card2))

    def test_can_get_highest_card(self):
        self.assertEqual(self.card1, self.cardGame.highest_card(
            self.card1, self.card2))

    def test_can_get_cards_total(self):
        cards = [self.card1, self.card2, self.card]

        self.assertEqual("You have a total of11",
                         self.cardGame.cards_total(cards))


if __name__ == '__main__':
    unittest.main()
