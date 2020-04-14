'''
IMPORTS
'''

import time
import black_jack_helper as bjh

'''
WELCOME MESSAGE
'''
print('Welcome to Black Jack!')
time.sleep(1)
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('Let\'s go!')


'''
CHIPS BANK
'''

pl_total_chips = 0

while pl_total_chips <= 0:

    while True:

        try:
            total_chips_inp = int(input('Give me the total amount of chips you have: '))
        except:
            print('That needs to be an integer number')
            time.sleep(2)
        else:
            break

    if total_chips_inp > 0:

        pl_total_chips += total_chips_inp
        time.sleep(2)
        break

    else:

        print('This needs to be a number greater than 0')
        time.sleep(2)

pl_chips_bank = bjh.ChipsBank(total=pl_total_chips)

# keep a record of the initial amount of chips, this will be handy to work out the net gain/loss at the end
pl_total_chips_initial = pl_total_chips

print(pl_chips_bank)


'''
Game while loop begins
'''
while True:

    # Begin the game

    # Create the deck
    my_deck = bjh.Deck()

    # Shuffle it
    my_deck.shuffle()

    # Ask for bet
    my_bet = bjh.ask_bet(pl_chips_bank)

    # Deal 2 cards to dealer, 2 cards to player
    pl_card_1 = my_deck.deal()
    pl_card_2 = my_deck.deal()
    de_card_1 = my_deck.deal()
    de_card_2 = my_deck.deal()

    print("This is your first card: " + str(pl_card_1))
    time.sleep(2)

    print('This is your second card: ' + str(pl_card_2))
    time.sleep(2)

    print("This is the dealer's first card: " + str(de_card_1))
    time.sleep(2)

    print('The dealer\'s second card is hidden')
    time.sleep(2)

    # Add the cards to the player's hand
    pl_hand = bjh.Hand()
    pl_hand.add_card(pl_card_1)
    pl_hand.add_card(pl_card_2)
    print(pl_hand)

    # Add cards to the dealer's hand
    de_hand = bjh.Hand()
    de_hand.add_card(de_card_1)
    de_hand.add_card(de_card_2)

    # Begin player's turn
    while pl_hand.value < 21:

        # Ask if player wants to hit
        while True:

            while True:
                try:
                    hit_resp = str(input('Do you want to hit? y/n ')).upper()
                except:
                    print('Please reply with a string \'y\' or \'no\'')
                else:
                    break

            if hit_resp == 'Y' or hit_resp == 'N':

                break

            else:
                print('Please reply with a string \'y\' or \'no\'')

        # if yes, add the card to the hand and desplay the hand
        if hit_resp == 'Y':
            pl_new_card = my_deck.deal()

            pl_hand.add_card(pl_new_card)

            print(pl_hand)
            time.sleep(2)

        # if not, break the while and continue
        if hit_resp == 'N':
            break

    # if the hand's value has gone above 21, then substract bet and continue to the next iteration
    if pl_hand.value > 21:

        print('BUST!!!\nEnd of this match')
        time.sleep(2)
        pl_chips_bank.lose_bet(my_bet)

        if bjh.continue_playing(pl_chips_bank):
            continue
        else:
            print('End of the game. You are going home with: \n' + str(pl_chips_bank.total))
            break

    print('It is now the dealer\'s turn')
    time.sleep(2)

    print('As we said, the dealer\'s first card is: \n' + str(de_card_1))
    time.sleep(2)

    print('We can now show you the dealer\'s second card too: \n' + str(de_card_2))
    time.sleep(2)

    print('So the total value of the dealer\'s hand is: \n' + str(de_hand.value))
    time.sleep(2)

    while de_hand.value < 17:
        de_new_card = my_deck.deal()
        print('The dealer has just got a: \n' + str(de_new_card))
        time.sleep(2)

        de_hand.add_card(de_new_card)
        print('The dealer\'s hand is now worth: ' + str(de_hand.value))
        time.sleep(2)

    if de_hand.value > 21:

        print('The dealer has gone BUST! You win the game!')

        pl_chips_bank.win_bet(my_bet)
        time.sleep(2)

        if bjh.continue_playing(pl_chips_bank):
            continue
        else:
            print('End of the game. You are going home with: \n' + str(pl_chips_bank.total))
            break

    elif de_hand.value > pl_hand.value:

        print('The dealer has won. Dealer\'s hand is worth: \n' + str(de_hand.value) + '\nYour hand is worth: \n' + str(
            pl_hand.value))
        pl_chips_bank.lose_bet(my_bet)
        time.sleep(2)

        if bjh.continue_playing(pl_chips_bank):
            continue
        else:
            print('End of the game. You are going home with: \n' + str(pl_chips_bank.total))
            break

    elif de_hand.value < pl_hand.value:

        print('You won. Dealer\'s hand is worth: \n' + str(de_hand.value) + '\nYour hand is worth: \n' + str(
            pl_hand.value))
        pl_chips_bank.win_bet(my_bet)
        time.sleep(2)

        if bjh.continue_playing(pl_chips_bank):
            continue
        else:
            print('End of the game. You are going home with: \n' + str(pl_chips_bank.total))
            break

    elif de_hand.value == pl_hand.value:

        print('You draw. Dealer\'s hand is worth: \n' + str(de_hand.value) + '\nYour hand is worth: \n' + str(
            pl_hand.value))
        time.sleep(2)

        if bjh.continue_playing(pl_chips_bank):
            continue
        else:
            print('End of the game. You are going home with: \n' + str(pl_chips_bank.total))
            break
