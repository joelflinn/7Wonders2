from django.test import TestCase
from django.contrib.auth.models import User
from wonders_app.models import *

class ModelTestClass(TestCase):
    @classmethod

    def setUp(self):

        self.player = Player.objects.create(
            name = "test",
            number_of_wins = 5, 
        )

        self.board = Board.objects.create(
            name = "test board",
            board_type = "giza",
            win_or_loss = "WIN",
            score = 34
        )

        self.Card = Card.objects.create(
            name = "test card",
            add_to_board = True,
            pointValue = 3,
            card_image = "well.PNG"
        )



    def test_false_is_false(self):
        print("testing the player model")
        self.assertEqual(self.player.name, 'test')

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)