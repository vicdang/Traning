import pygame
import random

pygame.init()
suits = ['heart', 'diamond', 'club', 'spade']
groups = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
specials = ['Black Joker', 'Red Joker']

deck_clubs = [pygame.image.load('card_pack\\Clubs 1.png'), pygame.image.load('card_pack\\Clubs 2.png'), pygame.image.load('card_pack\\Clubs 3.png'),
              pygame.image.load('card_pack\\Clubs 4.png'), pygame.image.load('card_pack\\Clubs 5.png'), pygame.image.load('card_pack\\Clubs 6.png'),
              pygame.image.load('card_pack\\Clubs 7.png'),
              pygame.image.load('card_pack\\Clubs 8.png'), pygame.image.load('card_pack\\Clubs 9.png'), pygame.image.load('card_pack\\Clubs 10.png'),
              pygame.image.load('card_pack\\Clubs 11.png'),
              pygame.image.load('card_pack\\Clubs 12.png'), pygame.image.load('card_pack\\Clubs 13.png')]
deck_diamonds = [pygame.image.load('card_pack\\Diamond 1.png'), pygame.image.load('card_pack\\Diamond 2.png'),
                 pygame.image.load('card_pack\\Diamond 3.png'), pygame.image.load('card_pack\\Diamond 4.png'),
                 pygame.image.load('card_pack\\Diamond 5.png'), pygame.image.load('card_pack\\Diamond 6.png'),
                 pygame.image.load('card_pack\\Diamond 7.png'), pygame.image.load('card_pack\\Diamond 8.png'),
                 pygame.image.load('card_pack\\Diamond 9.png'),
                 pygame.image.load('card_pack\\Diamond 10.png'), pygame.image.load('card_pack\\Diamond 11.png'),
                 pygame.image.load('card_pack\\Diamond 12.png'), pygame.image.load('card_pack\\Diamond 13.png')]
deck_hearts = [pygame.image.load('card_pack\\Hearts 1.png'), pygame.image.load('card_pack\\Hearts 2.png'), pygame.image.load('card_pack\\Hearts 3.png'),
               pygame.image.load('card_pack\\Hearts 4.png'), pygame.image.load('card_pack\\Hearts 5.png'), pygame.image.load('card_pack\\Hearts 6.png'),
               pygame.image.load('card_pack\\Hearts 7.png'),
               pygame.image.load('card_pack\\Hearts 8.png'), pygame.image.load('card_pack\\Hearts 9.png'), pygame.image.load('card_pack\\Hearts 10.png'),
               pygame.image.load('card_pack\\Hearts 11.png'), pygame.image.load('card_pack\\Hearts 12.png'),
               pygame.image.load('card_pack\\Hearts 13.png')]
deck_spades = [pygame.image.load('card_pack\\Spades 1.png'), pygame.image.load('card_pack\\Spades 2.png'), pygame.image.load('card_pack\\Spades 3.png'),
               pygame.image.load('card_pack\\Spades 4.png'), pygame.image.load('card_pack\\Spades 5.png'), pygame.image.load('card_pack\\Spades 6.png'),
               pygame.image.load('card_pack\\Spades 7.png'),
               pygame.image.load('card_pack\\Spades 8.png'), pygame.image.load('card_pack\\Spades 9.png'), pygame.image.load('card_pack\\Spades 10.png'),
               pygame.image.load('card_pack\\Spades 11.png'),
               pygame.image.load('card_pack\\Spades 12.png'), pygame.image.load('card_pack\\Spades 13.png')]
deck_specials = [pygame.image.load('card_pack\\z black Joker.png'), pygame.image.load('card_pack\\z red Joker.png')]

card_images = [deck_hearts, deck_diamonds, deck_clubs, deck_spades, deck_specials]
card_back = pygame.image.load('card_pack\\card_back.png')
font = pygame.font.Font(None, 20)
pygame.font.init()

class Card:
    def __init__(self, *args):
        if len(args) == 2:
            self.group = args[0]
            self.suit = args[1]
            self.special = None
        elif len(args) == 1:
            self.group = None
            self.suit = None
            self.special = args[0]
        else:
            self.group = None
            self.suit = None
            self.special = None

    def __repr__(self):
        if self.special is not None:
            return "{}".format(self.special)
        elif self.group is not None and self.suit is not None:
            return "{} {}".format(self.group, self.suit)
        else:
            return ""

class Game(object):
    def __init__(self):
        self.deck = []
        for group in groups:
            for suit in suits:
                # 52 cards combined of 4 Suites and 13 groups
                self.deck.append(Card(group, suit))
        for special in specials:
            # 2 special cards
            self.deck.append(Card(special))
        self.hand1 = None   # Player hand
        self.hand2 = None   # House hand
        self.remainingCards = 54
        self.gameover = False

    def shuffle_deck(self):
        random.shuffle(self.deck)
        return self.deck
    
    def deal_hand1(self, surf):
        self.hand1 = self.deck.pop()
        self.remainingCards-=1
        # move cardback to Player hand
        back_fill(surf, ((winWidth//2-cardWidth//2)-2, (winHeight-cardHeight-50)-2, 50, 65))
        surf.blit(card_back, ((winWidth//2-cardWidth//2), (winHeight-cardHeight-50)))
        return self.hand1

    def deal_hand2(self, surf):
        self.hand2 = self.deck.pop()
        self.remainingCards-=1
        # move cardback to House hand
        back_fill(surf, ((winWidth//2-cardWidth//2)-2, 48, 50, 65))
        surf.blit(card_back, ((winWidth//2-cardWidth//2), 50))
        return self.hand2

    def display_remaining_card(self, surf):
        pygame.draw.rect(surf, (164, 90, 82), deckArea)
        x_spacing = 0
        y = 150
        if 0 < self.remainingCards <= 18:
            for _ in range(self.remainingCards):
                surf.blit(card_back, (139 + x_spacing, y))
                x_spacing += 5
        elif 0 < self.remainingCards <= 36:
            for _ in range(18):
                surf.blit(card_back, (139 + x_spacing, y))
                x_spacing += 5
            x_spacing = 0
            for _ in range(self.remainingCards - 18):
                surf.blit(card_back, (139 + x_spacing, y-10))
                x_spacing += 5
        elif 0 < self.remainingCards <= 54:
            for _ in range(18):
                surf.blit(card_back, (139 + x_spacing, y))
                x_spacing += 5
            x_spacing = 0
            for _ in range(18):
                surf.blit(card_back, (139 + x_spacing, y-10))
                x_spacing += 5
            x_spacing = 0
            for _ in range(self.remainingCards - 36):
                surf.blit(card_back, (139 + x_spacing, y-20))
                x_spacing += 5

    def display_point_and_reward(self, surf, p):
        # display point
        back_fill(surf, point_rect)
        text = font.render("Points: {}".format(p.point), 1, (255, 255, 0))
        surf.blit(text, (24, winHeight//2 - 15))
        back_fill(surf, reward_rect)
        text = font.render("Reward: {}".format(p.reward), 1, (255, 255, 0))
        surf.blit(text, (20, winHeight//2))

    @staticmethod
    def compare_cards(c1, c2):
        sp = ["Red Joker", "Black Joker"]
        if c1.special == "Red Joker" and c2.special == "Black Joker":
            return c1
        if c1.special == "Black Joker" and c2.special == "Red Joker":
            return c2
        if c1.special in sp and c2.special not in sp:
            return c1
        if c1.special not in sp and c2.special in sp:
            return c2
        k = ["A", "K", "Q", "J"]
        if c1.group == "A" and c2.group == "A":
            if c1.suit == "heart":
                return c1
            if c2.suit == "heart":
                return c2
            if c1.suit == "spade":
                return c2
            if c2.suit == "spade":
                return c1
            if c1.suit == "diamond" and c2.suit == "club":
                return c1
            if c1.suit == "club" and c2.suit == "diamond":
                return c2
        if c1.group == "A" and c2.group == "K":
            return c1
        if c1.group == "A" and c2.group == "Q":
            return c1
        if c1.group == "A" and c2.group == "J":
            return c1
        if c1.group == "K" and c2.group == "A":
            return c2
        if c1.group == "K" and c2.group == "K":
            if c1.suit == "heart":
                return c1
            if c2.suit == "heart":
                return c2
            if c1.suit == "spade":
                return c2
            if c2.suit == "spade":
                return c1
            if c1.suit == "diamond" and c2.suit == "club":
                return c1
            if c1.suit == "club" and c2.suit == "diamond":
                return c2
        if c1.group == "K" and c2.group == "Q":
            return c1
        if c1.group == "K" and c2.group == "J":
            return c1
        if c1.group == "Q" and c2.group == "A":
            return c2
        if c1.group == "Q" and c2.group == "K":
            return c2
        if c1.group == "Q" and c2.group == "Q":
            if c1.suit == "heart":
                return c1
            if c2.suit == "heart":
                return c2
            if c1.suit == "spade":
                return c2
            if c2.suit == "spade":
                return c1
            if c1.suit == "diamond" and c2.suit == "club":
                return c1
            if c1.suit == "club" and c2.suit == "diamond":
                return c2
        if c1.group == "Q" and c2.group == "J":
            return c1
        if c1.group == "J" and c2.group == "A":
            return c2
        if c1.group == "J" and c2.group == "K":
            return c2
        if c1.group == "J" and c2.group == "Q":
            return c2
        if c1.group == "J" and c2.group == "J":
            if c1.suit == "heart":
                return c1
            if c2.suit == "heart":
                return c2
            if c1.suit == "spade":
                return c2
            if c2.suit == "spade":
                return c1
            if c1.suit == "diamond" and c2.suit == "club":
                return c1
            if c1.suit == "club" and c2.suit == "diamond":
                return c2
        if c1.group not in k and c2.group not in k:
            if int(c1.group) > int(c2.group):
                return c1
            if int(c1.group) == int(c2.group):
                if c1.suit == "heart":
                    return c1
                if c2.suit == "heart":
                    return c2
                if c1.suit == "spade":
                    return c2
                if c2.suit == "spade":
                    return c1
                if c1.suit == "diamond" and c2.suit == "club":
                    return c1
                if c1.suit == "club" and c2.suit == "diamond":
                    return c2
            if int(c1.group) < int(c2.group):
                return c2
        if c1.group in k and c2.group not in k:
            return c1
        if c1.group not in k and c2.group in k:
            return c2

class Player(object):
    def __init__(self):
        self.receivedCard = None
        self.houseCard = None
        self.started = False
        self.guess_high_card = None
        self.guessing = False
        self.winning = False
        self.losing = False
        self.deciding = False
        self.cont = None
        self.point = 60
        self.reward = 0
        self.multi_correct = False

    def show_card(self, surf):
        if self.receivedCard.special == 'Black Joker':
            back_fill(surf, ((winWidth//2-cardWidth//2)-2, (winHeight-cardHeight-50)-2, 50, 65))
            pygame.display.update()
            pygame.time.delay(1000)
            surf.blit(card_images[4][0], ((winWidth//2-cardWidth//2), (winHeight-cardHeight-50)))
        elif self.receivedCard.special == 'Red Joker':
            back_fill(surf, ((winWidth//2-cardWidth//2)-2, (winHeight-cardHeight-50)-2, 50, 65))
            pygame.display.update()
            pygame.time.delay(1000)
            surf.blit(card_images[4][1], ((winWidth//2-cardWidth//2), (winHeight-cardHeight-50)))
        else:
            k = 0
            j = 0
            for s in suits:
                if self.receivedCard.suit == s:
                    for g in groups:
                        if self.receivedCard.group == g:
                            back_fill(surf, ((winWidth//2-cardWidth//2)-2, (winHeight-cardHeight-50)-2, 50, 65))
                            pygame.display.update()
                            pygame.time.delay(1000)
                            surf.blit(card_images[j][k], ((winWidth//2-cardWidth//2), (winHeight-cardHeight-50)))
                        if k <= 12:
                            k += 1
                if j <= 3:
                    j += 1

    def guess_higher(self):
        self.guess_high_card = self.receivedCard

    def guess_lower(self):
        self.guess_high_card = self.houseCard

    def decide_cont(self):
        self.cont = True

    def decide_stop(self):
        self.cont = False

class House(object):
    def __init__(self):
        receivedCard = None

    def show_card(self, surf, p):
        p.houseCard = self.receivedCard
        if self.receivedCard.special == 'Black Joker':
            back_fill(surf, ((winWidth//2-cardWidth//2)-2, 48, 50, 65))
            pygame.display.update()
            pygame.time.delay(1000)
            surf.blit(card_images[4][0], ((winWidth//2-cardWidth//2), 50))
        elif self.receivedCard.special == 'Red Joker':
            back_fill(surf, ((winWidth//2-cardWidth//2)-2, 48, 50, 65))
            pygame.display.update()
            pygame.time.delay(1000)
            surf.blit(card_images[4][1], ((winWidth//2-cardWidth//2), 50))
        else:
            k = 0
            j = 0
            for s in suits:
                if self.receivedCard.suit == s:
                    for g in groups:
                        if self.receivedCard.group == g:
                            back_fill(surf, ((winWidth//2-cardWidth//2)-2, 48, 50, 65))
                            pygame.display.update()
                            pygame.time.delay(1000)
                            surf.blit(card_images[j][k], ((winWidth//2-cardWidth//2), 50))
                        if k <= 12:
                            k += 1
                if j <= 3:
                    j += 1

# Graphic
winWidth = 400
winHeight = 400
cardWidth = 47
cardHeight = 62

deckArea = (134, 125, 142, 92)
playing_rect = (winWidth//2 - 170, 230, 340, 60)
point_rect = (20, winHeight//2 -15 , 100, 15) 
reward_rect = (20, winHeight//2, 100, 15)

def back_fill(surf, rectangle):
    color = (0,0,0)
    pygame.draw.rect(surf, color, rectangle)

def draw_layout(surf, g, p):
    pygame.draw.rect(surf, (255, 0, 0), (10, 10, 380, 380), 2)
    pygame.draw.rect(surf, (164, 90, 82), deckArea)
    g.display_remaining_card(surf)
    if not p.started:
        back_fill(surf, playing_rect)
        # draw start button
        pygame.draw.circle(surf, (0, 200, 50), (winWidth//2, 257), 20)
        text = font.render("START", 1, (255, 255, 255))
        surf.blit(text, (winWidth//2 -21, 250))
    if p.guessing:
        back_fill(surf, playing_rect)
        text = font.render("Make your guess", 1, (255, 255, 0))
        # draw Higher button
        surf.blit(text, (winWidth//2 - 50, 235))
        pygame.draw.circle(surf, (0, 255, 0), (winWidth//2 - 85, 267), 10)
        text = font.render("Higher", 1, (255, 255, 0))
        surf.blit(text, (winWidth//2 - 65, 260))
        # draw Lower button
        pygame.draw.circle(surf, (0, 0, 255), (winWidth//2 + 45, 267), 10)
        text = font.render("Lower", 1, (255, 255, 0))
        surf.blit(text, (winWidth//2 + 65, 260))
    if p.deciding:
        back_fill(surf, playing_rect)
        # draw Continue button
        pygame.draw.rect(surf, (0, 200, 50), (winWidth//2 - 30, 235, 60, 15))
        text = font.render("Continue", 1, (255, 255, 255))
        surf.blit(text, (winWidth//2 - 27, 235))
        # draw Stop button
        pygame.draw.rect(surf, (255, 0, 0), (winWidth//2 - 30, 260, 60, 15))
        text = font.render("Stop", 1, (255, 255, 255))
        surf.blit(text, (winWidth//2 - 15, 260))
    g.display_point_and_reward(surf, p)
    pygame.display.update()
