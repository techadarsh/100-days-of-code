# Blackjack Project Guide (Day 11)

## Choose Your Difficulty
- **Normal 😎**: Use all hints below to complete the project.
- **Hard 🤔**: Use only Hints **1, 2, 3** to complete the project.
- **Extra Hard 😭**: Use only Hints **1 & 2** to complete the project.
- **Expert 🤯**: Use only Hint **1** to complete the project.

---

## Our Blackjack Game House Rules
- The deck is **unlimited** in size.
- There are **no jokers**.
- **Jack / Queen / King** all count as **10**.
- **Ace** can count as **11** or **1**.
- Use the following list as the deck of cards:

```text
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```

- Each card in the list has **equal probability** of being drawn.
- Cards are **not removed** from the deck as they are drawn.
- The computer is the **dealer**.

---

## Hint 1
Try out Blackjack here:
- https://games.washingtonpost.com/games/blackjack/

Then try the completed demo here:
- https://appbrewery.github.io/python-day11-demo/

---

## Hint 2
Read the breakdown of program requirements:
- http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

Then create your own flowchart for the program.

## Blackjack Requirements Checklist

- [ ] Deal both user and computer a starting hand of 2 random card values.
- [ ] Detect when computer or user has a blackjack (Ace + 10 value card).
- [ ] If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a blackjack, then they win (unless the computer also has a blackjack).
- [ ] Calculate the user's and computer's scores based on their card values.
- [ ] If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
- [ ] Reveal computer's first card to the user.
- [ ] Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
- [ ] Ask the user if they want to get another card.
- [ ] Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16.
- [ ] Compare user and computer scores and see if it's a win, loss, or draw.
- [ ] Print out the player's and computer's final hand and their scores at the end of the game.
- [ ] After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.

---

## Hint 3
Download and read the flow chart:
- https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Blackjack Simple Steps (from Flowchart)

## Simple Steps
1. Start the game.
2. Deal **2 random cards** to the user and **2 random cards** to the computer.
3. Calculate both scores.
4. Check **blackjack**:
   - If **user has blackjack (Ace + 10)** → User wins.
   - Else if **computer has blackjack** → User loses.
5. If user score > 21:
   - If user has an Ace (11), convert Ace from **11 to 1** and recalculate.
   - If still > 21 → User loses.
6. Ask the user: **"Do you want another card?"**
   - If yes → deal 1 more card to user, recalculate score, go back to step 4/5.
   - If no → continue to dealer turn.
7. Dealer (computer) plays:
   - While computer score < 17 → deal another card and recalculate.
8. If computer score > 21 → User wins.
9. Compare final scores:
   - Same score → Draw
   - User score higher → User wins
   - User score lower → User loses


# Blackjack Text Flowchart

START
  |
  v
Deal 2 cards to User and 2 cards to Computer
  |
  v
Calculate User score + Computer score
  |
  v
Does User or Computer have Blackjack (Ace + 10)?
  |
  |-- YES --> User has Blackjack? ---- YES --> WIN
  |            |
  |            NO
  |            v
  |        Computer has Blackjack? --> YES --> LOSE
  |
  NO
  |
  v
Is User score > 21?
  |
  |-- NO --> Ask User: "Draw another card?"
  |            |
  |            |-- YES --> Deal 1 card to User --> Calculate score --> (Back to Blackjack check)
  |            |
  |            NO
  |            v
  |        Computer plays:
  |        While Computer score < 17:
  |            Deal 1 card to Computer
  |            Recalculate score
  |            |
  |            v
  |     Has Computer score > 21?
  |         |
  |         |-- YES --> WIN
  |         |
  |         NO
  |         |
  |         v
  |     Compare scores:
  |        |-- Same score  --> DRAW
  |        |-- User higher --> WIN
  |        |-- User lower  --> LOSE
  |
 YES
  |
  v
Does User have an Ace (11)?
  |    
  |-- NO --> LOSE
  |
 YES
  |
  v
Convert one Ace from 11 to 1, recalculate score
  |
  v
Still User score > 21?
  |
  |-- YES --> LOSE
  |
  NO --> Go to "Ask User: Draw another card?"

---

## Hint 4
Create a function `deal_card()` that returns a random card from:

```text
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```

Note: `11` represents the Ace.

---

## Hint 5
Deal 2 cards to the user and computer using `deal_card()` and `append()`:

```text
user_cards = []
computer_cards = []
```

---

## Hint 6
Create a function `calculate_score()` that takes a list of cards and returns the score.
Tip: Use Python’s `sum()`.

---

## Hint 7
Inside `calculate_score()`, check for Blackjack:
- A hand with only **2 cards**: **Ace (11) + 10**
- Return **0** instead of actual score  
  (0 will represent Blackjack in this game)

---

## Hint 8
Inside `calculate_score()`, handle Ace (11):
- If score is over 21 and there is an 11 in the hand,
  - remove 11 and replace it with 1

Reference:
- https://developers.google.com/edu/python/lists#list-methods

---

## Hint 9
Call `calculate_score()`.
If any of these is true, the game ends:
- User has Blackjack (0)
- Computer has Blackjack (0)
- User score is over 21

---

## Hint 10
If the game has not ended:
Ask the user if they want to draw another card.
- If yes: use `deal_card()` and add it to `user_cards`
- If no: the game ends for the user

---

## Hint 11
Recheck the score after every new card:
Repeat Hint 9 checks until the game ends.

---

## Hint 12
Computer’s turn (dealer rules):
- The computer keeps drawing cards as long as its score is **less than 17**

---

## Hint 13
Create a function `compare(user_score, computer_score)`:

Rules:
- If both scores are the same → **Draw**
- If computer has Blackjack (0) → **User loses**
- If user has Blackjack (0) → **User wins**
- If user_score > 21 → **User loses**
- If computer_score > 21 → **User wins**
- Otherwise, highest score wins

---

## Hint 14
Ask the user if they want to restart the game:
- If yes: clear the console and start again
- Show the logo from `art.py` at the start