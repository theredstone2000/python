import pygame
import random

# Initialiser pygame
pygame.init()

# Paramètres de la fenêtre
largeur = 600
hauteur = 400
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu Snake")

# Couleurs
vert_clair = (144, 238, 144)
rouge = (255, 0, 0)
orange = (255, 165, 0)

# Paramètres du serpent
taille_serpent = 10
serpent = [[100, 50]]
direction = "DROITE"

# Paramètres de la nourriture
nourriture = [random.randrange(1, largeur // taille_serpent) * taille_serpent,
              random.randrange(1, hauteur // taille_serpent) * taille_serpent]

# Fonction pour dessiner le serpent
def dessiner_serpent(serpent):
    for segment in serpent:
        pygame.draw.rect(screen, rouge, pygame.Rect(segment[0], segment[1], taille_serpent, taille_serpent))

# Boucle principale du jeu
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and direction != "BAISSE":
                direction = "HAUT"
            elif event.key == pygame.K_s and direction != "HAUT":
                direction = "BAISSE"
            elif event.key == pygame.K_q and direction != "DROITE":
                direction = "GAUCHE"
            elif event.key == pygame.K_d and direction != "GAUCHE":
                direction = "DROITE"

    # Déplacer le serpent
    if direction == "HAUT":
        nouvelle_tete = [serpent[0][0], serpent[0][1] - taille_serpent]
    elif direction == "BAISSE":
        nouvelle_tete = [serpent[0][0], serpent[0][1] + taille_serpent]
    elif direction == "GAUCHE":
        nouvelle_tete = [serpent[0][0] - taille_serpent, serpent[0][1]]
    elif direction == "DROITE":
        nouvelle_tete = [serpent[0][0] + taille_serpent, serpent[0][1]]

    serpent.insert(0, nouvelle_tete)

    # Vérifier la collision avec la nourriture
    if serpent[0] == nourriture:
        nourriture = [random.randrange(1, largeur // taille_serpent) * taille_serpent,
                      random.randrange(1, hauteur // taille_serpent) * taille_serpent]
    else:
        serpent.pop()

    # Vérifier les collisions avec les bords
    if (serpent[0][0] < 0 or serpent[0][0] >= largeur or
        serpent[0][1] < 0 or serpent[0][1] >= hauteur):
        break  # Fin du jeu

    # Dessiner le fond, le serpent et la nourriture
    screen.fill(vert_clair)
    dessiner_serpent(serpent)
    pygame.draw.rect(screen, orange, pygame.Rect(nourriture[0], nourriture[1], taille_serpent, taille_serpent))
    pygame.display.flip()

    # Limiter la vitesse du jeu
    clock.tick(15)

# Quitter pygame
pygame.quit()
