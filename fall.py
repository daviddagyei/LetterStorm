import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('LetterStorm')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game settings
LETTER_FALL_SPEED = 5
NEW_LETTER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(NEW_LETTER_EVENT, 1000)  # Spawn a new letter every second

# Fonts
FONT = pygame.font.Font(None, 74)
SCORE_FONT = pygame.font.Font(None, 36)

# Load assets
BACKGROUND_IMAGE = pygame.image.load('background.png')
SCORE_SOUND = pygame.mixer.Sound('score.mp3')

# Letter class
class Letter:
    def __init__(self):
        self.char = chr(random.randint(65, 90))  # Random uppercase letter
        self.x = random.randint(0, SCREEN_WIDTH - 50)
        self.y = -50
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def move(self):
        self.y += LETTER_FALL_SPEED
        self.rect.y = self.y

    def draw(self):
        text = FONT.render(self.char, True, WHITE)
        SCREEN.blit(text, (self.x, self.y))

# Display message on the screen
def display_message(text, font, color, x, y):
    message = font.render(text, True, color)
    rect = message.get_rect(center=(x, y))
    SCREEN.blit(message, rect)

# Start screen
def show_start_screen():
    SCREEN.fill(BLACK)
    display_message("Falling Letters", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
    display_message("Press any key to start", SCORE_FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False

# Game over screen
def show_game_over_screen(score):
    SCREEN.fill(BLACK)
    display_message("Game Over", FONT, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
    display_message(f"Final Score: {score}", SCORE_FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    pygame.display.flip()
    pygame.time.wait(3000)

# Game loop
def main():
    clock = pygame.time.Clock()
    letters = []
    score = 0
    missed_letters = 0

    show_start_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == NEW_LETTER_EVENT:
                letters.append(Letter())
            if event.type == pygame.KEYDOWN:
                for letter in letters:
                    if event.unicode.upper() == letter.char:
                        letters.remove(letter)
                        score += 1
                        SCORE_SOUND.play()
                        break

        for letter in letters:
            letter.move()
            if letter.y > SCREEN_HEIGHT:
                missed_letters += 1
                letters.remove(letter)
                if missed_letters >= 3:
                    show_game_over_screen(score)
                    pygame.quit()
                    sys.exit()

        # Draw everything
        SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
        for letter in letters:
            letter.draw()

        # Display score
        score_text = SCORE_FONT.render(f"Score: {score}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))

        # Display missed letters
        missed_text = SCORE_FONT.render(f"Missed: {missed_letters}", True, RED)
        SCREEN.blit(missed_text, (10, 50))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
