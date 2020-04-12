import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        ret = self.rank + ' of ' + self.suit
        return ret


class Deck:

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                card = Card(suit=suit, rank=rank)
                self.deck.append(card)

    def __str__(self):
        string_return = "".join([str(x) + "\n" for x in self.deck])
        return string_return

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):

        deal_return = self.deck[0]
        del self.deck[0]
        return deal_return


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces_count = 0

    def __str__(self):
        string_return = "".join([str(x) + "\n" for x in self.cards])

        string_return = 'These are the cards currently in your hand:\n' + string_return \
                        + '\nAnd this is the total value of your hand atm:\n' + str(self.value)

        return string_return

    def add_card(self, card):

        # add the card to the hand
        self.cards.append(card)

        # get the rank of the card
        card_rank = card.rank

        # if the card is an ace, increment the count
        if card_rank == 'Ace':
            self.aces_count += 1

        # figure out the card value
        card_value = values[card_rank]

        '''
        If we have 1 ace in the hand (so far), then we want the ace to be counted as value 11.
        If we have 2 aces in the hand, then we want the second one to be counted as value 1.
        We never want both aces to be counted as 11s, as the hand would go bust, while
        if we only have 1 ace, we never want that to be counted as 1 as that would keep us further away from 21.
        We do not need to ask the user what they want to do with the aces as this is always the optimal strategy.
        '''
        if self.aces_count <= 1:

            self.value += card_value

        elif self.aces_count == 2:

            self.value += 1


class ChipsBank:

    def __init__(self, total=100):
        self.total = total

    def __str__(self):
        return 'The total amount of chips atm is ' + str(self.total)

    def win_bet(self, bet):
        self.total += bet
        print('You just won ' + str(bet) + '\nThe total amount of chips is now ' + str(self.total))

    def lose_bet(self, bet):
        self.total -= bet
        print('You just lost ' + str(bet) + '\nThe total amount of chips is now ' + str(self.total))


def ask_bet(my_chips_bank):
    bet = 0

    while bet <= 0:

        while True:

            try:
                bet = int(input('How many chips do you want to bet? '))
            except:
                time.sleep(1)
                print('That is not an integer number, just try again')
            else:
                break

        if bet > my_chips_bank.total:
            time.sleep(1)
            print('You do not have that much money')
            bet = 0
            print(my_chips_bank)
        else:
            time.sleep(1)
            print('Ok, we got your bet. Let\'s continue')
            return bet


def continue_playing(my_chips_bank):
    cont_res = ''

    if my_chips_bank.total == 0:
        print('You have run out of chips.')
        cont_res = 'N'

    while cont_res != 'Y' and cont_res != 'N':

        cont_res = str(input('Do you want to continue playing? y/n ')).upper()

        if cont_res != 'Y' and cont_res != 'N':
            print('please enter \'y\' or \'n\'')

    if cont_res == 'Y':
        return True
    else:
        return False
