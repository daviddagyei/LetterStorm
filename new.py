import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Falling Letters')

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

# Game loop
def main():
    clock = pygame.time.Clock()
    letters = []
    score = 0
    missed_letters = 0

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
                        break

        for letter in letters:
            letter.move()
            if letter.y > SCREEN_HEIGHT:
                missed_letters += 1
                letters.remove(letter)
                if missed_letters >= 3:
                    pygame.quit()
                    print(f"Game Over! Final Score: {score}")
                    sys.exit()

        # Draw everything
        SCREEN.fill(BLACK)
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
