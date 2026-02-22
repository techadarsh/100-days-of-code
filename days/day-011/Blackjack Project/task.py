import random
import art

# Grouped by rank -> suit variants in this exact order:
# [CLUBS(+), DIAMONDS(O), HEARTS(#), SPADES(@)]
CARD_ART_BY_RANK = {
    "A": [art.ACE_PLUS, art.ACE_O, art.ACE_HASH, art.ACE_AT],
    "K": [art.KING_PLUS, art.KING_O, art.KING_HASH, art.KING_AT],
    "Q": [art.QUEEN_PLUS, art.QUEEN_O, art.QUEEN_HASH, art.QUEEN_AT],
    "J": [art.JACK_PLUS, art.JACK_O, art.JACK_HASH, art.JACK_AT],
    "10": [art.TEN_PLUS, art.TEN_O, art.TEN_HASH, art.TEN_AT],
    "9": [art.NINE_PLUS, art.NINE_O, art.NINE_HASH, art.NINE_AT],
    "8": [art.EIGHT_PLUS, art.EIGHT_O, art.EIGHT_HASH, art.EIGHT_AT],
    "7": [art.SEVEN_PLUS, art.SEVEN_O, art.SEVEN_HASH, art.SEVEN_AT],
    "6": [art.SIX_PLUS, art.SIX_O, art.SIX_HASH, art.SIX_AT],
    "5": [art.FIVE_PLUS, art.FIVE_O, art.FIVE_HASH, art.FIVE_AT],
    "4": [art.FOUR_PLUS, art.FOUR_O, art.FOUR_HASH, art.FOUR_AT],
    "3": [art.THREE_PLUS, art.THREE_O, art.THREE_HASH, art.THREE_AT],
    "2": [art.TWO_PLUS, art.TWO_O, art.TWO_HASH, art.TWO_AT],
}

# Mapping of blackjack numeric value -> possible ranks to display
# Use this when you draw a number from cards = [11,2..10,10,10,10]
VALUE_TO_RANKS = {
    11: ["A"],
    10: ["10", "J", "Q", "K"],
    9: ["9"],
    8: ["8"],
    7: ["7"],
    6: ["6"],
    5: ["5"],
    4: ["4"],
    3: ["3"],
    2: ["2"],
    1: ["A"],
}

def print_cards_horizontal(card_arts, gap="   "):
    # Split each card into lines
    cards_lines = []
    widths = []

    for art in card_arts:
        lines = art.splitlines()
        cards_lines.append(lines)

        max_w = 0
        for ln in lines:
            if len(ln) > max_w:
                max_w = len(ln)
        widths.append(max_w)

    # Find max height (line count) among all cards
    max_h = 0
    for lines in cards_lines:
        if len(lines) > max_h:
            max_h = len(lines)

    # Print line by line with padding
    for i in range(max_h):
        row_parts = []
        for idx, lines in enumerate(cards_lines):
            w = widths[idx]
            if i < len(lines):
                row_parts.append(lines[i].ljust(w))
            else:
                row_parts.append(" " * w)
        print(gap.join(row_parts))

def deal_card():
    """
    Returns a Random card from the deck
    :return:
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    take a list of cards and calculate the score
    return the score of the given cards
    :param cards:
    :return:
    """
    # if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def get_ascii_art_of_card(cards, card_back):
    ascii_art = []
    if not card_back:
        for card_number in cards:
            ascii_art.append(random.choice(CARD_ART_BY_RANK[random.choice(VALUE_TO_RANKS[card_number])]))
    else :
        # for computer player specially when we don't have to reveal all cards
        ascii_art.append(random.choice(CARD_ART_BY_RANK[random.choice(VALUE_TO_RANKS[cards[0]])]))
        ascii_art.append(art.CARD_BACK)
    return ascii_art

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, Opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went Over. You lose"
    elif c_score > 21:
        return "Opponent went Over. You win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Loose"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}, Current Score: {user_score}")
        # print cards ascii art for computer
        print_cards_horizontal(get_ascii_art_of_card(cards=user_cards, card_back=False))
        print(f"Computer's First Card: {computer_cards[0]}")
        # print cards ascii art for computer
        print_cards_horizontal(get_ascii_art_of_card(cards=computer_cards, card_back=True))

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, and final score: {user_score}")
    print_cards_horizontal(get_ascii_art_of_card(cards=user_cards, card_back=False))
    print(f"Computer's first hand: {computer_cards}, and final score: {computer_score}")
    print_cards_horizontal(get_ascii_art_of_card(cards=computer_cards, card_back=False))
    print(compare(user_score, computer_score))

while input("Do you want to play again? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20000)
    play_game()
