import random

balance = 500
VALUES = {"A": 11,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 10,"Q": 10,"K": 10}

def hand_value(hand):
    total = 0
    aces = 0
    for rank, suit in hand:
        total += VALUES[rank]
        if rank == "A":
            aces += 1
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


def display_hand(hand):
    return " ".join([rank + suit for rank, suit in hand])

    '''
    for card in hand:
        print(card[0] + card[1], end=" ")

    print()'''

def hit(hand):
    hand.append(cards.pop())

def dealer_turn():
    while hand_value(dealer) < 17:
        dealer.append(cards.pop())

while True:

    print("\n" + "=" * 40)
    print("BALANCE:", balance)

    if balance <= 0:
        print("You are broke.")
        break

    bet = int(input("Enter bet: "))

    if bet > balance:
        print("Insufficient funds.")
        continue

    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["A", "2", "3", "4", "5", "6","7", "8", "9", "10", "J", "Q", "K"]

    cards = []

    for suit in suits:
        for rank in ranks:
            cards.append((rank, suit))

    random.shuffle(cards)

    player = []
    dealer = []

    player.append(cards.pop())
    dealer.append(cards.pop())

    player.append(cards.pop())
    dealer.append(cards.pop())

    print("\nYour Hand:")
    print(display_hand(player))
    print("Value:", hand_value(player))

    print("\nDealer Shows:")
    print(dealer[0][0] + dealer[0][1])

    if hand_value(player) == 21 and len(player) == 2:
        print("\nBLACKJACK")

        if hand_value(dealer) == 21:
            print("Push.")

        else:
            profit = int(bet * 1.5)
            balance += profit
            print(f"You win {profit}")

        again = input("\nPlay again? (y/n): ")
        if again.lower() != "y":
            break
        continue

    split_hands = []
    can_split = (player[0][0] == player[1][0])
    player_done = False

    while not player_done:

        print("\nYour Hand:")
        print(display_hand(player))
        print("Value:", hand_value(player))

        if hand_value(player) > 21:
            print("BUST")
            balance -= bet
            player_done = True
            break

        menu = "\nHit(H) Stand(S) Double(D)"

        if can_split:
            menu += " Split(P)"

        choice = input(menu + "\n").upper()

        if choice == "H":
            hit(player)

        elif choice == "S":
            player_done = True

        elif choice == "D":
            if balance >= bet:
                bet *= 2
                hit(player)
                print(display_hand(player))

                if hand_value(player) > 21:

                    print("BUST")
                    balance -= bet
                    player_done = True
                    break

                player_done = True
            else:

                print("Not enough balance.")

        elif choice == "P" and can_split:

            hand1 = [player[0]]
            hand2 = [player[1]]
            hit(hand1)
            hit(hand2)

            split_hands = [hand1, hand2]
            player_done = True

        else:
            print("Invalid choice.")

    if split_hands:
        dealer_turn()

        for number, hand in enumerate(split_hands, start=1):
            print(f"\nPlaying Split Hand {number}")
            while hand_value(hand) < 17:
                break

            player_total = hand_value(hand)
            dealer_total = hand_value(dealer)

            print("Hand:", display_hand(hand))
            print("Value:", player_total)

            if player_total > 21:
                balance -= bet

            elif dealer_total > 21:
                balance += bet

            elif player_total > dealer_total:
                balance += bet

            elif dealer_total > player_total:
                balance -= bet

            else:
                pass

    elif hand_value(player) <= 21:

        dealer_turn()

        player_total = hand_value(player)
        dealer_total = hand_value(dealer)

        print("\nDealer Hand:")
        print(display_hand(dealer))
        print("Dealer Value:", dealer_total)
        print("\nYour Value:", player_total)

        if dealer_total > 21:
            print("Dealer Busts!")
            balance += bet

        elif player_total > dealer_total:
            print("You Win!")
            balance += bet

        elif dealer_total > player_total:
            print("Dealer Wins!")
            balance -= bet

        else:
            print("Push.")

    print("\nCurrent Balance:", balance)
    again = input("\nPlay Again? (y/n): ")
    if again.lower() != "y":
        break

print("\nFinal Balance:", balance)