import random
import pandas as pd
from data_vis.card_logic import CardLogic 

class ClashRoyaleGame:
    def __init__(self):
        self.player1_tower_health = 1000
        self.player2_tower_health = 1000
        self.player1_deck = ['Zap', 'The Log', 'Fireball', 'Arrows', 'Mega Knight', 'Skeleton Armys', 'Valkyrie', 'Wizard']
        self.player2_deck = self.get_player2_cards()

        # Initialize player hands
        self.player1_hand_size = 4
        self.player1_hand = self.draw_cards(self.player1_deck, self.player1_hand_size)

        self.player2_hand_size = 4  # Player 2 starts with 4 cards in hand
        self.player2_hand = self.draw_cards(self.player2_deck, self.player2_hand_size)

        # Instantiate the CardLogic class
        self.card_logic = CardLogic()

    def get_player2_cards(self):
        # Read cards from CSV file for Player 2
        player2_card_data = pd.read_csv(r'C:\Users\Cdog1\OneDrive\Documents\MEM 680T\Final Visuals\Data_vis\src\data_vis\datapath\500266047.csv')  # Replace with your actual CSV file path
        player2_deck = player2_card_data['team.card1.name'].tolist()

        # Ensure Player 2 starts with 8 cards from the CSV file
        starting_hand_size = 8
        player2_hand = self.draw_cards(player2_deck, starting_hand_size)

        return player2_deck

    def draw_cards(self, deck, num_cards):
        # Draw a specified number of cards from the deck
        drawn_cards = random.sample(deck, num_cards)
        return drawn_cards

    def display_game_state(self, player_hand):
        print(f"Player 1 Tower Health: {self.player1_tower_health}")
        print(f"Player 2 Tower Health: {self.player2_tower_health}")

        if player_hand == self.player1_hand:
            print(f"Player 1 Hand: {player_hand}")
        elif player_hand == self.player2_hand:
            print(f"Player 2 Hand: {player_hand}")

    def player_turn(self, player_deck, player_hand):
        
        selected_card = input("Choose a card to deploy (type 'exit' to end the game): ")

        if selected_card.lower() == 'exit':
            print("Game ended by player.")
            exit()

        if selected_card not in player_hand:
            print("Invalid card selection. Try again.")
            return self.player_turn(player_deck, player_hand)

        # Call the corresponding card logic function based on the selected card
    
        temp_selected_card = selected_card.replace(" ", "_").replace(".", "").replace("-", "_").lower()
        card_logic_function = getattr(self.card_logic, f"{temp_selected_card}_logic", None)
        if card_logic_function:
            card_result = card_logic_function()
            if isinstance(card_result, dict):
                damage = card_result.get('damage', 0)  # Assuming default damage is 0 if not present in the dictionary
                # Handle any additional logic or effects here...
                print("Amount of Damage:", damage)
            else:
                damage = card_result
                print("Amount of Damage:", damage)
            return selected_card, damage
        else:
            print("Invalid card logic. Try again.")
            return self.player_turn(player_deck, player_hand)


    def update_player_hand(self, player_deck, player_hand, used_card):
        # Move the used card to the back of the deck
        player_deck.remove(used_card)
        player_deck.append(used_card)

        # Draw a new card from the deck that is not in the current hand
        new_card = random.choice([card for card in player_deck if card not in player_hand])
        player_hand.remove(used_card)
        player_hand.append(new_card)

    def play(self):
        while self.player1_tower_health > 0 and self.player2_tower_health > 0:
            print("\n=== Player 1's Turn ===")
            self.display_game_state(self.player1_hand)  # Pass the current player's hand to display_game_state
            player1_card, player1_damage = self.player_turn(self.player1_deck, self.player1_hand)
            self.player2_tower_health -= player1_damage
            self.update_player_hand(self.player1_deck, self.player1_hand, player1_card)

            if self.player2_tower_health <= 0:
                print("Player 1 wins!")
                break

            print("\n=== Player 2's Turn ===")
            self.display_game_state(self.player2_hand)  # Pass the current player's hand to display_game_state
            player2_card, player2_damage = self.player_turn(self.player2_deck, self.player2_hand)
            self.player1_tower_health -= player2_damage
            self.update_player_hand(self.player2_deck, self.player2_hand, player2_card)

            if self.player1_tower_health <= 0:
                print("Player 2 wins!")
                break

    def test_card_logic(self):
        all_cards = self.player1_deck + self.player2_deck

        for card in all_cards:
            card_name = card.lower().replace(" ", "_")
            card_logic_function = getattr(self.card_logic, f"{card_name}_logic", None)

            if card_logic_function:
                try:
                    card_result = card_logic_function()
                    if not isinstance(card_result, (int, dict)):
                        print(f"Error: Invalid result for {card}")
                except Exception as e:
                    print(f"Error: Exception in {card} logic - {e}")
            else:
                print(f"Error: Missing logic for {card}")

    
if __name__ == "__main__":
    game = ClashRoyaleGame()
    game.play() 