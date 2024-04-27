import random
import os
import time


class Card:                                         #We used a card class to use it later.

    def __init__(self, face, value, symbol):
        self.face = face
        self.value = value
        self.symbol = symbol


def display_cards(cards, hidden):                     #With cards parameter display_cards function will draw cards for us by display_cars function even it's hidden(?)
    s = ''
    for card in cards:
        s = s + '\t ________________'
    if hidden:
        s += '\t ________________'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        if card.face in ['J', 'Q', 'K', 'A']:            #We wrote the 10 point cards here(J,Q,K,A).
            s = s + '\t|  {}             |'.format(card.face)
        elif card.value == 10:                          #The 10 point card too.
            s = s + '\t|  {}            |'.format(card.value)
        else:
            s = s + '\t|  {}             |'.format(card.value)

    if hidden:                                         #Hidden card
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:                                  #We continue to draw cards but hidden one should be a question mark.
        s = s + '\t|                |'
    if hidden:
        s += '\t|      * *       |'
    print(s)

    s = ''
    for card in cards:                                  #Continues
        s = s + '\t|                |'
    if hidden:
        s += '\t|    *     *     |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|   *       *    |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|   *       *    |'
    print(s)

    s = ''
    for card in cards:                                          #In the middle of the card we decided to put a symbol.
        s = s + '\t|       {}        |'.format(card.symbol)
    if hidden:                                                  #Of course not for the hidden one.
        s += '\t|          *     |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|         *      |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|        *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:                                        #The  end of the card display should look like this.
        if card.face in ['J', 'Q', 'K', 'A']:
            s = s + '\t|            {}   |'.format(card.face)
        elif card.value == 10:
            s = s + '\t|           {}   |'.format(card.value)
        else:
            s = s + '\t|            {}   |'.format(card.value)
    if hidden:
        s += '\t|        *       |'
    print(s)

    s = ''
    for card in cards:                                         #The end of display_cards function.
        s = s + '\t|________________|'
    if hidden:
        s += '\t|________________|'
    print(s)
    print()


                                                                #With imported random we decided to make a function that selects a card from the deck and removes it so, it won't come again.
def deal_card(deck):
    card = random.choice(deck)                                  #The choice() function constructs a random item from a list, tuple, or string expression.
    deck.remove(card)
    return card, deck


def play_blackjack(deck):
    player_hand = []                                            #This lists are going to be blank when it's started.
    dealer_hand = []
    player_score = 0
    dealer_score = 0
    os.system('clear')

    while len(player_hand) < 2:                                 #This loop deals cards to the player.
        player_card, deck = deal_card(deck)
        player_hand.append(player_card)
        player_score += player_card.value

                                                                # If dealt a second Ace, adjusts player score.
        if len(player_hand) == 2:
            if player_hand[0].value == 11 and player_hand[1].value == 11: #Ace will be counted as 1 or 11.
                player_hand[0].value = 1
                player_score -= 10

        print('PLAYER CARDS: ')
        display_cards(player_hand, False)                       #This function will display cards but not the hidden one.
        print('PLAYER SCORE = ', player_score)

        input('Continue...')

        dealer_card, deck = deal_card(deck)
        dealer_hand.append(dealer_card)
        dealer_score += dealer_card.value

                                                                # If dealt a second Ace, adjust dealer score. Adjusts 2nd card to hide that the dealer has an Ace.

        if len(dealer_hand) == 2:
            if dealer_hand[0].value == 11 and dealer_hand[1].value == 11:
                dealer_hand[1].value = 1
                dealer_score -= 10

        print('DEALER CARDS: ')
        if len(dealer_hand) == 1:
            display_cards(dealer_hand, False)
            print('DEALER SCORE = ', dealer_score)
        else:
            display_cards(dealer_hand[:-1], True)
            print('DEALER SCORE = ', dealer_score - dealer_hand[-1].value)

        input('Continue...')

    if player_score == 21:
        print('PLAYER HAS A BLACKJACK!!!!')                      #If player hits a blackjack it prints this.
        print('PLAYER WINS!!!!')
        time.sleep(5)
        quit()
    os.system('clear')

    print('DEALER CARDS: ')
    display_cards(dealer_hand[:-1], True)                         #When the game ends, all the dealer's cards are revealed (except the last one, which is hidden).
    print('DEALER SCORE = ', dealer_score - dealer_hand[-1].value)#All the player's cards and score are shown
    print()
    print('PLAYER CARDS: ')
    display_cards(player_hand, False)
    print('PLAYER SCORE = ', player_score)

    while player_score < 21:
        choice = input('Enter H to Hit or S to Stand: ').upper() #Player will draw cards till this input.
        if len(choice) != 1 or (choice not in ['H', 'S']):       #If player makes a invalid choice. It prints 'Invalid choice!! Try Again...'
            os.system('clear')
            print('Invalid choice!! Try Again...')
            continue

        if choice.upper() == 'S':                                #If player stands with his decision(S). Loop breaks. And dealer reveals the hidden.
            break
        else:
            player_card, deck = deal_card(deck)
            player_hand.append(player_card)
            player_score += player_card.value
            card_pos = 0

                                                                    # If dealt an Ace, adjust score for each existing Ace in hand.
            while player_score > 21 and card_pos < len(player_hand):
                if player_hand[card_pos].value == 11:
                    player_hand[card_pos].value = 1                 #The Ace will counted as 11 if total is not over 21. If not it counted as 1.
                    player_score -= 10                              #So we rearrange the numbers.
                    card_pos += 1
                else:
                    card_pos += 1

            if player_score > 21:                                   #If player score above 21 player loses.                                 
                break

            os.system('clear')                                      #Clears the system.
            print('DEALER CARDS: ')
            display_cards(dealer_hand[:-1], True)                   #Reveals the hidden card.
            print('DEALER SCORE = ', dealer_score - dealer_hand[-1].value) #BATU BURAYI ANLAMADIM BURAYI ANLARSAN YAZ KNK!!!
            print()
            print('PLAYER CARDS: ')
            display_cards(player_hand, False)
            print('PLAYER SCORE = ', player_score)                    #Prints player score.

    os.system('clear')
    print('PLAYER CARDS: ')
    display_cards(player_hand, False)
    print('PLAYER SCORE = ', player_score)
    print()
    print('DEALER IS REVEALING THEIR CARDS....')
    print('DEALER CARDS: ')
    display_cards(dealer_hand, False)
    print('DEALER SCORE = ', dealer_score)

    if player_score == 21:                                          #If the first dealt cards equals 21 player wins instantly.
        print('PLAYER HAS A BLACKJACK, PLAYER WINS!!!')
        time.sleep(5)
        quit()

    if player_score > 21:                               
        print('PLAYER BUSTED!!! GAME OVER!!!')                      #If player score above 21 player loses.  
        time.sleep(5)
        quit()

    input('Continue...')
    while dealer_score < 17:                                              #Dealer has to draw cards till it equals 17 or more.
        os.system('clear')
        print('DEALER DECIDES TO HIT.....')
        dealer_card, deck = deal_card(deck)
        dealer_hand.append(dealer_card)
        dealer_score += dealer_card.value

                                                                        #If dealt an Ace, adjust score for each existing Ace in hand.
        card_pos = 0
        while dealer_score > 21 and card_pos < len(dealer_hand):
            if dealer_hand[card_pos].value == 11:                       #The Ace will counted as 11 if total is not over 21. If not it counted as 1.
                dealer_hand[card_pos].value = 1                         #So we rearrange the numbers.
                dealer_score -= 10
                card_pos += 1
            else:
                card_pos += 1

        print('PLAYER CARDS: ')
        display_cards(player_hand, False)
        print('PLAYER SCORE = ', player_score)
        print()
        print('DEALER CARDS: ')
        display_cards(dealer_hand, False)
        print('DEALER SCORE = ', dealer_score)
        if dealer_score > 21:                                           
            break
        input('Continue...')

    if dealer_score > 21:                                               #If dealer's score more than 21 you win.
        print('DEALER BUSTED!!! YOU WIN!!!')
        time.sleep(5)
        quit()
    elif dealer_score == 21:                                            #If dealer's score is 21 at the first place dealer wins.
        print('DEALER HAS A BLACKJACK!!! PLAYER LOSES!!!')
        time.sleep(5)
        quit()
    elif dealer_score == player_score:                                  #If player and dealer has the same score its a tie.
        print('TIE GAME!!!!')
    elif player_score > dealer_score:                                   #If player's score more than dealer's score (not over 21) player wins.
        print('PLAYER WINS!!!')
    else:
        print('DEALER WINS!!!')                                         #Else dealer wins.


def initialize_deck():
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
                                                                            #We used UNICODE values for card symbol images.
    suit_symbols = {'Hearts': '\u2661', 'Diamonds': '\u2662',
                    'Spades': '\u2664', 'Clubs': '\u2667'}
    cards = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,               #The values written here.
             '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    deck = []
    for suit in suits:
        for card, value in cards.items():
            deck.append(Card(card, value, suit_symbols[suit]))
    return deck



game_deck = initialize_deck()               #A deck of cards is created with game_deck = initialize_deck().
play_blackjack(game_deck)                   #The game starts with play_blackjack(game_deck) function we wrote at the first place and the main loop of the game runs.