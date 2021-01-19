Game
  |- deck (52 cards combined of 4 Suites and 13 groups + 2 special cards = 54 cards)
  |- hand1 (hand to deal to Player)
  |- hand2 (hand to deal to House)
  |- remainingCard
  |- Gameover
  |- def shuffle_deck(used to random 54 cards)
  |- def deal_hand1(used to deal card to Player)
  |- def deal_hand2(used to deal card to House)
  |- def display_remaining_card
  |- def display_point_and_reward
  |- def compare_cards
  
Player
  |- receivedCard = None
  |- houseCard = None (Card that house shows to Player)
  |- started = False
  |- guess_high_card = None
  |- guessing = False
  |- winning = False
  |- losing = False
  |- deciding = False
  |- cont = None
  |- point = 60
  |- reward = 0
  |- multi_correct = False
  |- def show_card
  |- def guess_higher
  |- def guess_lower
  |- def decide_cont
  |- def decide_stop
  
House
  |- receivedCard
  |- show_card