
def bid_max(game_spec, diamond_card):
    if diamond_card == 13 and len(game_spec.PRIME_CARDS) < 3:
            bot_card = max(game_spec.BOT_CARD)
            return bot_card
    return False
    
def bid_aggression(game_spec, diamond_card):
     if game_spec.Opponent_aggression >= 1:
            min_score = float('inf')  # Initialize min_score to infinity
            chosen_card = None  # Initialize chosen_card to None

            for card in game_spec.BOT_CARD:
                if card > diamond_card:
                    diff = abs(card - diamond_card)
                    beat_count = sum(1 for opp_card in game_spec.OPPONENT_CARD if opp_card > card)
                    score = diff * (beat_count + 2)

                    if score < min_score:
                        min_score = score
                        chosen_card = card

            return chosen_card if chosen_card is not None else min(game_spec.BOT_CARD)  # Return the chosen card or the lowest available card
     else:
          return min(game_spec.BOT_CARD)  # Return the lowest available card if aggression level is not high enough


def bid_exception(game_spec, diamond_card):
    if diamond_card in [7, 8, 9]:
        game_spec.Opponent_aggression = 2
        return bid_aggression(game_spec, diamond_card)
    return False
