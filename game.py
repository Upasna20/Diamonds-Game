import random
import strategies

class Game:
    def __init__(self):
        self.ROUND = 1
        self.SCORE_USER = self.SCORE_BOT = 0
        self.DIAMOND_CARD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.BOT_CARD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.OPPONENT_CARD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.PRIME_CARDS = [10, 11, 12, 13]
        self.Opponent_aggression = 0
        self.agg_frequency = 0
        self.agg_consistency = 0
        self.curr_card = None

    def set_round(self):
        self.ROUND += 1

    def get_round(self):
        return self.ROUND

    def get_bot_score(self):
        return self.SCORE_BOT

    def get_user_score(self):
        return self.SCORE_USER
    
    def update_OppCard(self, val):
        self.OPPONENT_CARD.remove(val)

    def choose_diamond(self):
        diamond_card_value = random.choice(self.DIAMOND_CARD)
        self.DIAMOND_CARD.remove(diamond_card_value)
        return diamond_card_value
    
    def update_aggressiveness(self, diamond_card, Opp_card):
        if  Opp_card > diamond_card:
            self.agg_frequency += 1
            self.agg_consistency += 1
        elif self.agg_consistency > 0:  # Decrease consistency only if it's greater than 0
            self.agg_consistency -= 1

        self.Opponent_aggression = (self.agg_frequency + self.agg_consistency) / self.ROUND

        if Opp_card in self.PRIME_CARDS:
            self.PRIME_CARDS.remove(Opp_card)  # Remove prime card if opponent wins it

        if len(self.PRIME_CARDS) < 3:
            self.Opponent_aggression = 2

    def choose_botcard(self, diamond_card):
        
        if strategies.bid_max(game_spec, diamond_card):
            self.curr_card = strategies.bid_max(game_spec, diamond_card)
        elif strategies.bid_exception(game_spec, diamond_card):
            self.curr_card = strategies.bid_exception(game_spec, diamond_card)
        else:
            self.curr_card = strategies.bid_aggression(game_spec, diamond_card)
 


        self.BOT_CARD.remove(self.curr_card)
        return self.curr_card
        
    
    def evaluate_round(self, opponent_card, bot_card, diamond_value):
        if bot_card > opponent_card:
            self.SCORE_BOT += diamond_value
        elif bot_card < opponent_card:
            self.SCORE_USER += diamond_value
        else:
            self.SCORE_BOT += diamond_value / 2
            self.SCORE_USER += diamond_value / 2

    
    def res_round(self, opponent_card, bot_card):
        if opponent_card == bot_card: return 0
        return -1 if opponent_card - bot_card > 0 else 1
    
    def verdict(self):
        if self.SCORE_BOT == self.SCORE_USER: return 0
        return -1 if self.SCORE_USER > self.SCORE_BOT else 1
        


        




game_spec = Game()










# def update_score(val: either 0 or 1):
    # pass

def evaluate_round(user_card):
    pass
    # opponent_strategy apply and get the bot's card
    # then take the user_card and compare them
    # if user wins return 0 , 1 for bot and 2 for draw
