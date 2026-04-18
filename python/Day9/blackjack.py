import random
         
def deal_card():
    '''Returns a random card from the deck'''
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  
    return sum(cards)

def compare(u_score, d_score):
    if u_score == d_score:
        return "Draw"
    elif d_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "You win with Blackjack!!!"
    elif u_score > 21:
        return "You busted!"
    elif d_score > 21:
        return "Dealer Busts, you win!!!"
    elif u_score > d_score:
        return "You win!!!"
    else:
        return "You lose"


def play_game():
    user_cards = []
    dealer_cards = []
    dealer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)
    play_game()
