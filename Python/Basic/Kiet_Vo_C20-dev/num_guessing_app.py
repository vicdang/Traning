from components import *
import pygame
import sys
import random

pygame.init()

game = None
player = None
house = None

def initialize_game():
    global game, player, house
    
    game = Game()
    player = Player()
    house = House()

    game.shuffle_deck()

initialize_game()

win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Number Guessing App")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Wait until start pressed
        if event.type == pygame.MOUSEBUTTONDOWN and not game.gameover and not player.started:
            if pygame.mouse.get_pressed()[0]:
                # start button position
                if (winWidth//2 - 20) <= pygame.mouse.get_pos()[0] <= (winWidth//2 + 20):
                    if 237 <= pygame.mouse.get_pos()[1] <= 277:
                        player.started = True
                        player.cont = True

        # Game start or Player decide to continue
        if not game.gameover and player.started and player.cont and not player.guessing and not player.deciding:
            if game.remainingCards ==0:
                game = Game()
                game.shuffle_deck()
            # Player and the House receive 01 card from the deck
            back_fill(win, playing_rect)
            house.receivedCard = game.deal_hand2(win)
            player.receivedCard = game.deal_hand1(win)
            game.display_remaining_card(win)
            pygame.display.update()
            pygame.time.delay(1000)
            # House shows card first
            house.show_card(win, player)
            player.guessing = True

        # Player start guessing
        if event.type == pygame.MOUSEBUTTONDOWN and not game.gameover and player.guessing:
            if pygame.mouse.get_pressed()[0]:
                # Higher button position
                if (winWidth//2 - 95) <= pygame.mouse.get_pos()[0] <= (winWidth//2 - 75):
                    if 257 <= pygame.mouse.get_pos()[1] <= 277:
                        back_fill(win, playing_rect)
                        player.guess_higher()   # Player guess higher
                        player.show_card(win)
                        high_card = game.compare_cards(player.receivedCard, house.receivedCard)
                        # Player is correct
                        if high_card == player.guess_high_card:
                            text = font.render("You win, take the money", 1, (255, 255, 0))
                            win.blit(text, (winWidth//2 - 73, 250))
                            if player.multi_correct:
                                player.reward *= 2
                            else:
                                player.reward = 20
                            player.multi_correct = True
                        # Player is wrong
                        else:
                            text = font.render("You lose, give me your money", 1, (255, 255, 0))
                            win.blit(text, (winWidth//2 - 90, 250))
                            player.point -= 25
                            player.reward = 0
                            player.multi_correct = False
                        game.display_point_and_reward(win, player)
                        pygame.display.update()
                        pygame.time.delay(4000)
                        # check win lose condition
                        if (player.point + player.reward) >= 1000:
                            player.winning = True
                        elif player.point < 30:
                            player.losing = True
                        else:
                            player.deciding = True
                        player.guessing = False
                # Lower button position
                if (winWidth//2 + 35) <= pygame.mouse.get_pos()[0] <= (winWidth//2 + 55):
                    if 257 <= pygame.mouse.get_pos()[1] <= 277:
                        back_fill(win, playing_rect)
                        player.guess_lower()    # Player guess higher
                        player.show_card(win)
                        high_card = game.compare_cards(player.receivedCard, house.receivedCard)
                        # Player is correct
                        if high_card == player.guess_high_card:
                            text = font.render("You win, take the money", 1, (255, 255, 0))
                            win.blit(text, (winWidth//2 - 73, 250))
                            if player.multi_correct:
                                player.reward *= 2
                            else:
                                player.reward = 20
                            player.multi_correct = True
                        # Player is wrong
                        else:
                            text = font.render("You lose, give me your money", 1, (255, 255, 0))
                            win.blit(text, (winWidth//2 - 90, 250))
                            player.point -= 25
                            player.reward = 0
                            player.multi_correct = False
                        game.display_point_and_reward(win, player)
                        pygame.display.update()
                        pygame.time.delay(4000)
                        # check win lose condition
                        if (player.point + player.reward) >= 1000:
                            player.winning = True
                        elif player.point < 30:
                            player.losing = True
                        else:
                            player.deciding = True
                        player.guessing = False

        # Player wins
        if not game.gameover and player.winning:
            # Player earn reward
            player.point += player.reward
            # Show winning message
            back_fill(win, playing_rect)
            text = font.render("You earn {}. Time to close. No more money for you!".format(player.point), 1, (255, 0, 0))
            win.blit(text, (winWidth//2 - 170, 235))
            text = font.render("<Press space to reset game>".format(player.point), 1, (255, 0, 0))
            win.blit(text, (winWidth//2 - 85, 260))
            game.gameover = True
            back_fill(win, ((winWidth//2-cardWidth//2)-2, 48, 50, 65))
            back_fill(win, ((winWidth//2-cardWidth//2)-2, (winHeight-cardHeight-50)-2, 50, 65))

        # Player loses
        if not game.gameover and player.losing:
            # Player has no reward
            player.point += player.reward
            # Show losing message
            back_fill(win, playing_rect)
            text = font.render("You're out of money. Go home and get some!".format(player.point), 1, (255, 0, 0))
            win.blit(text, (winWidth//2 - 135, 235))
            text = font.render("<Press space to reset game>".format(player.point), 1, (255, 0, 0))
            win.blit(text, (winWidth//2 - 85, 260))
            game.gameover = True
            back_fill(win, ((winWidth//2-cardWidth//2)-2, 48, 50, 65))
            back_fill(win, ((winWidth//2-cardWidth//2)-2, (winHeight-cardHeight-50)-2, 50, 65))

        # Player decide continue or stop
        if event.type == pygame.MOUSEBUTTONDOWN and not game.gameover and player.deciding:
            if pygame.mouse.get_pressed()[0]:
                # Continue button position
                if (winWidth//2 - 30) <= pygame.mouse.get_pos()[0] <= (winWidth//2 + 30):
                    if 235 <= pygame.mouse.get_pos()[1] <= 250:
                        back_fill(win, playing_rect)
                        player.decide_cont()
                        player.deciding = False

                # Stop button position
                if (winWidth//2 - 30) <= pygame.mouse.get_pos()[0] <= (winWidth//2 + 30):
                    if 260 <= pygame.mouse.get_pos()[1] <= 275:
                        back_fill(win, playing_rect)
                        player.decide_stop()
                        player.deciding = False

        # Player decide to stop
        if not game.gameover and player.started and not player.cont:
            # Player earn reward
            player.point += player.reward
            # Show stop message
            back_fill(win, playing_rect)
            text = font.render("Game ends. You earn {}".format(player.point), 1, (255, 0, 0))
            win.blit(text, (winWidth//2 - 80, 235))
            text = font.render("<Press space to reset game>".format(player.point), 1, (255, 0, 0))
            win.blit(text, (winWidth//2 - 85, 260))
            game.gameover = True
            back_fill(win, ((winWidth//2-cardWidth//2)-2, 48, 50, 65))
            back_fill(win, ((winWidth//2-cardWidth//2)-2, (winHeight-cardHeight-50)-2, 50, 65))

        # Game over, player press space to reset game
        if event.type == pygame.KEYDOWN and game.gameover:
            if event.key == pygame.K_SPACE:
                initialize_game()
                gameOver = False

    draw_layout(win, game, player)
