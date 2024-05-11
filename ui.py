import pygame
import sys
import game 
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

def load_main_screen():
    # Load background image (if desired)
    background_image = pygame.image.load('images/aditya-chinchure-IEISYENbXp8-unsplash.jpg').convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # Fonts and text
    heading_color = (238, 247, 255)  # RGB values corresponding to #EEF7FF
    button_color = (238, 247, 255)
    hover_color = (173, 216, 230)  # Color when mouse hovers over the button
    heading_font = pygame.font.Font(None, 90)
    button_font = pygame.font.Font(None, 32)
    heading_text = heading_font.render("Diamond Game", True, heading_color)
    play_text = button_font.render("Play", True, heading_color)  

    # Button dimensions and position (towards the bottom)
    button_width = 200
    button_height = 50
    button_x = (screen_width - button_width) // 2
    button_y = screen_height - button_height - 50  # Adjusted y position towards the bottom

    # Main loop
    running = True
    border_radius = 2
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:  # Mouse motion event
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if mouse is over the button
                if button_x <= mouse_x <= button_x + button_width and \
                button_y <= mouse_y <= button_y + button_height:
                    button_color = hover_color  # Change button color when hovered
                    play_text = button_font.render("Play", True, (0, 0, 0))  # Black text color
                    border_radius = 0
                else:
                    button_color = (238, 247, 255)  # Reset button color
                    play_text = button_font.render("Play", True, heading_color)  # Heading color for text
                    border_radius = 2
                    

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_x <= mouse_x <= button_x + button_width and \
                button_y <= mouse_y <= button_y + button_height:
                    return 0

        # Draw background image (if desired)
        screen.blit(background_image, (0, 0))

        # Draw heading text at the top
        heading_rect = heading_text.get_rect(center=(screen_width // 2, 100))  # Adjusted y position towards the top
        screen.blit(heading_text, heading_rect)

        # Draw play button with hover effect
        pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height), border_radius)
        button_rect = play_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(play_text, button_rect)

        pygame.display.update()

load_main_screen()

def load_game_screen():
    import pygame
    import sys
    import os

    # Initialize Pygame
    pygame.init()

    # Screen dimensions and padding
    screen_width = 1200
    screen_height = 700
    left_padding = 30
    right_padding = 30
    top_padding = 80
    bottom_padding = 50
    horizontal_padding = 20
    vertical_padding = 10
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Green background color
    background_color = (0, 128, 0)  # Green color


    # Load card images
    card_images = []
    spade_images = []
    card_names = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    card_starting_positions = {}  # Dictionary to store starting positions for each card
    row_height = 0  # Track the height of the current row
    current_x = left_padding  # Start from left padding
    current_y = top_padding  # Start from top padding
    for card_name in card_names:
        card_image_path = os.path.join('images/PNG-cards-1.3', f'{card_name}_of_hearts.png')
        spade_image_path = os.path.join('images/PNG-cards-1.3', f'{card_name}_of_spades.png')
        card_image = pygame.image.load(card_image_path).convert_alpha()
        spade_image = pygame.image.load(spade_image_path).convert_alpha()
        # Scale card images to fit within the screen width with padding
        scaled_width = (screen_width - left_padding - right_padding) // len(card_names)  # Calculate width for each card
        scaled_height = int(card_image.get_height() * (scaled_width / card_image.get_width()))  # Maintain aspect ratio
        card_image = pygame.transform.scale(card_image, (scaled_width, scaled_height))
        spade_image = pygame.transform.scale(spade_image, (scaled_width, scaled_height))
        card_images.append(card_image)
        spade_images.append(spade_image)

        # Check if adding this card exceeds the screen width, then move to the next row
        if current_x + scaled_width > screen_width - right_padding:
            current_x = left_padding  # Start from left padding for the new row
            current_y += row_height + vertical_padding  # Move to the next row
            row_height = 0  # Reset the row height

        card_starting_positions[card_name] = (current_x, current_y)  # Store card position in dictionary
        current_x += scaled_width + horizontal_padding  # Move to the next card position
        if scaled_height > row_height:
            row_height = scaled_height  # Update the row height if this card is taller


    # print(card_starting_positions)
    # Load diamond card images
    diamond_card_images = []
    diamond_card_names = ['ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    for card_name in diamond_card_names:
        card_image_path = os.path.join('images/PNG-cards-1.3', f'{card_name}_of_diamonds.png')
        card_image = pygame.image.load(card_image_path).convert_alpha()
        # Scale card images to fit within the screen width with padding
        scaled_width = (screen_width - left_padding - right_padding) // len(diamond_card_names)  # Calculate width for each card
        scaled_height = int(card_image.get_height() * (scaled_width / card_image.get_width()))  # Maintain aspect ratio
        card_image = pygame.transform.scale(card_image, (scaled_width, scaled_height))
        diamond_card_images.append(card_image)

    # Calculate card dimensions
    card_width = card_images[0].get_width()
    card_height = card_images[0].get_height()
    
    
    # Main loop
    running = True
    choosen_card = None
    show_message = True
    diamond_card_value = game.game_spec.choose_diamond()
    showResult = False
    while running:
        # if not game.game_spec.BOT_CARD:
        #     running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN and show_message:
                # print(event)
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, card_pos in enumerate(card_starting_positions.values()): 
                    card_x, card_y = card_pos
                    if card_x <= mouse_x <= card_x + card_width and card_y <= mouse_y <= card_y + card_height:
                        [choosen_card_face] = [card for card in card_starting_positions if card_starting_positions[card] == card_pos]
                        choosen_card = diamond_card_names.index(choosen_card_face) + 1
                        for key, value in card_starting_positions.items():
                            if value == card_pos:
                                del card_starting_positions [key]
                                break
                        game.game_spec.update_OppCard(choosen_card)
                        
                        bot_card = game.game_spec.choose_botcard(diamond_card_value)
                        game.game_spec.update_aggressiveness(diamond_card_value, choosen_card)
                        game.game_spec.evaluate_round(choosen_card, bot_card, diamond_card_value)
                        showResult = True
                        
                        show_message = False

                        if game.game_spec.DIAMOND_CARD:

                            diamond_card_value = game.game_spec.choose_diamond()
                            
                            game.game_spec.set_round()

                        
                        break




        # Fill screen with green color
        screen.fill(background_color)

        # Load font for text display
        font = pygame.font.Font(None, 36)


        # Display "Your Cards" text
        if game.game_spec.BOT_CARD:

             # Display "Round:" text above cards
            round_text = font.render(f"Round: {game.game_spec.get_round()}", True, (243, 202, 82))  # White color text, update round number as needed
            round_rect = round_text.get_rect(midtop=(screen_width // 2, top_padding - 60))  # Position above the cards row
            screen.blit(round_text, round_rect)

            # Display bot and user scores
            bot_score_text = font.render(f"Bot Score: {game.game_spec.SCORE_BOT}", True, (255, 255, 255))  # White color text
            user_score_text = font.render(f"Your Score: {game.game_spec.SCORE_USER}", True, (255, 255, 255))  # White color text
            bot_score_rect = bot_score_text.get_rect(midtop=(screen_width // 4, screen_height - 50))
            user_score_rect = user_score_text.get_rect(midtop=(3 * screen_width // 4, screen_height - 50))
            screen.blit(bot_score_text, bot_score_rect)
            screen.blit(user_score_text, user_score_rect)
            text = font.render("Your Cards", True, (255, 255, 255))  # White color text
            text_rect = text.get_rect(topleft=(left_padding, top_padding - 30))  # Position above the cards row
            screen.blit(text, text_rect)

        # Display cards in rows with padding
        x_pos = left_padding
        y_pos = top_padding
        for card_name, (x, y) in card_starting_positions.items():
            card_image = card_images[card_names.index(card_name)]  # Get the corresponding card image
            screen.blit(card_image, (x, y))  # Display card at its position
            x_pos = x
            y_pos = y
        
        if game.game_spec.BOT_CARD:
            # Display "Diamond Card Value" text below cards
            value_text = font.render("Diamond Card Value", True, (255, 255, 255))  # White color text
            value_rect = value_text.get_rect(midleft=(left_padding, y_pos + card_height + vertical_padding + 20))  # Position towards the left of the screen
            screen.blit(value_text, value_rect)

            # Display a randomly chosen diamond card image below "Diamond Card Value" text
            diamond_card = diamond_card_images[diamond_card_value - 1]
            diamond_card_rect = diamond_card.get_rect(bottomleft=(left_padding, value_rect.bottom + 150))  # Position below "Diamond Card Value" text
            screen.blit(diamond_card, diamond_card_rect)

            card_value_dict = {1: "ace", 11: "jack", 12: "queen", 13: "king"}
            if showResult:
                bot_card_value = bot_card
                if bot_card in [1, 11, 12, 13]:
                    bot_card_value = card_value_dict[bot_card]
                bot_card_image = card_images[card_names.index(choosen_card_face)]
                user_card_image = spade_images[card_names.index(str(bot_card_value))]

                # Calculate the width of the combined bot and user cards plus spacing
                combined_width = bot_card_image.get_width() + user_card_image.get_width() + 20  # Add 20 for spacing

                # Calculate the leftmost position for the combined cards to center them horizontally
                combined_x = (screen_width - combined_width) // 2

                # Position the bot card to the left of the center
                bot_card_rect = bot_card_image.get_rect(midleft=(combined_x, screen_height - 200))  # Adjusted y-coordinate

                # Position the user card to the right of the bot card with spacing
                user_card_rect = user_card_image.get_rect(midleft=(bot_card_rect.right + 10, bot_card_rect.centery))

                # Blit the bot card and user card at their respective rects
                screen.blit(bot_card_image, bot_card_rect)
                screen.blit(user_card_image, user_card_rect)

                res = game.game_spec.res_round(choosen_card, bot_card)
                if res == 0:
                    sentence_text = font.render("TIE!!", True, (255, 255, 255))  # White color text
                if res == 1:
                    sentence_text = font.render("BOT WINS THE ROUND!!", True, (255, 255, 255))  # White color text
                if res == -1:
                    sentence_text = font.render("YOU WIN THE ROUND!!", True, (255, 255, 255))  # White color text}}}}


                # Get the rect for the text surface
                sentence_rect = sentence_text.get_rect(midtop=(screen_width // 2, user_card_rect.top - 50))  # Adjusted y-coordinate

                # Blit the text surface onto the screen
                screen.blit(sentence_text, sentence_rect)

            


    

       

            show_message = True 
            if show_message:
                message_text = font.render("Choose a card against the diamond value", True, (255, 0, 0))  # Red color text
                message_rect = message_text.get_rect(center=(screen_width // 2, screen_height // 2))
                screen.blit(message_text, message_rect)

        
        if not game.game_spec.BOT_CARD:
            verdict = game.game_spec.verdict()
            if verdict == 0:
                sentence = "Match is a TIE, equal Scores."
            if verdict == 1:
                sentence = "Computer is the Winner!"
            else:
                sentence = "You Win!!"
            font = pygame.font.Font(None, 36)  # You can adjust the font size as needed

            # Create a text surface
            text_surface = font.render(sentence, True, (255, 255, 255))  # White color text

            # Get the rect for the text surface
            text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))  # Centered position

            # Blit the text surface onto the screen
            screen.blit(text_surface, text_rect)

        pygame.display.update()

    # Print the dictionary of card starting positions
    


load_game_screen()
