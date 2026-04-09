#!/usr/bin/env python3
"""
Small Pygame ball clicker.

Window title: "ballgame"
Background: white
Click the ball to change its color and increase the score.
"""
import sys
import random

import pygame


def main():
    pygame.init()
    pygame.font.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ballgame")

    clock = pygame.time.Clock()

    radius = 30
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 4
    dy = 3
    color = (200, 30, 30)

    score = 0

    font = pygame.font.SysFont(None, 36)
    background = (255, 255, 255)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                # squared distance check
                if (mx - x) * (mx - x) + (my - y) * (my - y) <= radius * radius:
                    score += 1
                    color = (
                        random.randint(40, 255),
                        random.randint(40, 255),
                        random.randint(40, 255),
                    )

        x += dx
        y += dy

        if x - radius <= 0:
            x = radius
            dx = -dx
        elif x + radius >= WIDTH:
            x = WIDTH - radius
            dx = -dx

        if y - radius <= 0:
            y = radius
            dy = -dy
        elif y + radius >= HEIGHT:
            y = HEIGHT - radius
            dy = -dy

        screen.fill(background)
        pygame.draw.circle(screen, color, (int(x), int(y)), radius)

        score_surf = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_surf, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
