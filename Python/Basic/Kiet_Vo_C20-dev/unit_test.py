import unittest
from components import Game
from components import Card

class TestStringMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass
    
    # Sort card from high to low
    # pop highest card and compare with other card. Expect return highest card
    # continue until no card left
    
    def test_compare_card_left(self):
        card_list = [["Red Joker"], ["Black Joker"], ["A", "heart"], ["A", "diamond"], ["A", "club"], ["A", "spade"], ["K", "heart"], ["K", "diamond"], ["K", "club"], ["K", "spade"], ["Q", "heart"], ["Q", "diamond"], ["Q", "club"], ["Q", "spade"], ["J", "heart"], ["J", "diamond"], ["J", "club"], ["J", "spade"], ["10", "heart"], ["10", "diamond"], ["10", "club"], ["10", "spade"], ["9", "heart"], ["9", "diamond"], ["9", "club"], ["9", "spade"], ["8", "heart"], ["8", "diamond"], ["8", "club"], ["8", "spade"], ["7", "heart"], ["7", "diamond"], ["7", "club"], ["7", "spade"], ["6", "heart"], ["6", "diamond"], ["6", "club"], ["6", "spade"], ["5", "heart"], ["5", "diamond"], ["5", "club"], ["5", "spade"], ["4", "heart"], ["4", "diamond"], ["4", "club"], ["4", "spade"], ["3", "heart"], ["3", "diamond"], ["3", "club"], ["3", "spade"], ["2", "heart"], ["2", "diamond"], ["2", "club"], ["2", "spade"]]
        while card_list:
            highest_card = card_list.pop(0)
            for other_card in card_list:
                #print "-------------------"
                #print highest_card
                #print other_card
                #print "-------------------"
                self.assertEqual(Game.compare_cards(Card(*highest_card), Card(*other_card)).group, Card(*highest_card).group)
                self.assertEqual(Game.compare_cards(Card(*highest_card), Card(*other_card)).suit, Card(*highest_card).suit)
                self.assertEqual(Game.compare_cards(Card(*highest_card), Card(*other_card)).special, Card(*highest_card).special)

    def test_compare_card_right(self):
        card_list = [["Red Joker"], ["Black Joker"], ["A", "heart"], ["A", "diamond"], ["A", "club"], ["A", "spade"], ["K", "heart"], ["K", "diamond"], ["K", "club"], ["K", "spade"], ["Q", "heart"], ["Q", "diamond"], ["Q", "club"], ["Q", "spade"], ["J", "heart"], ["J", "diamond"], ["J", "club"], ["J", "spade"], ["10", "heart"], ["10", "diamond"], ["10", "club"], ["10", "spade"], ["9", "heart"], ["9", "diamond"], ["9", "club"], ["9", "spade"], ["8", "heart"], ["8", "diamond"], ["8", "club"], ["8", "spade"], ["7", "heart"], ["7", "diamond"], ["7", "club"], ["7", "spade"], ["6", "heart"], ["6", "diamond"], ["6", "club"], ["6", "spade"], ["5", "heart"], ["5", "diamond"], ["5", "club"], ["5", "spade"], ["4", "heart"], ["4", "diamond"], ["4", "club"], ["4", "spade"], ["3", "heart"], ["3", "diamond"], ["3", "club"], ["3", "spade"], ["2", "heart"], ["2", "diamond"], ["2", "club"], ["2", "spade"]]
        while card_list:
            highest_card = card_list.pop(0)
            for other_card in card_list:
                #print "-------------------"
                #print other_card
                #print highest_card
                #print "-------------------"
                self.assertEqual(Game.compare_cards(Card(*other_card), Card(*highest_card)).group, Card(*highest_card).group)
                self.assertEqual(Game.compare_cards(Card(*other_card), Card(*highest_card)).suit, Card(*highest_card).suit)
                self.assertEqual(Game.compare_cards(Card(*other_card), Card(*highest_card)).special, Card(*highest_card).special)
  
if __name__ == '__main__': 
    unittest.main()
