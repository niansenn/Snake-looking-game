import pygame
import time
import random

# Initialisation de Pygame
pygame.init()

# Couleurs
blanc = (255, 255, 255)
jaune = (255, 255, 102)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (0, 255, 0)
bleu = (50, 153, 213)

# Dimensions de la fenêtre
largeur = 600
hauteur = 400

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Jeu Snake')

# Vitesse
horloge = pygame.time.Clock()
vitesse_snake = 15

# Taille du serpent
taille_snake = 10

# Police
police = pygame.font.SysFont("bahnschrift", 25)
score_police = pygame.font.SysFont("comicsansms", 35)

def afficher_score(score):
    valeur = score_police.render("Score: " + str(score), True, noir)
    fenetre.blit(valeur, [0, 0])

def dessiner_snake(taille_snake, liste_snake):
    for x in liste_snake:
        pygame.draw.rect(fenetre, noir, [x[0], x[1], taille_snake, taille_snake])

def message(msg, couleur):
    mesg = police.render(msg, True, couleur)
    fenetre.blit(mesg, [largeur / 6, hauteur / 3])

def dessiner_grille():
    for x in range(0, largeur, taille_snake):
        pygame.draw.line(fenetre, noir, (x, 0), (x, hauteur))
    for y in range(0, hauteur, taille_snake):
        pygame.draw.line(fenetre, noir, (0, y), (largeur, y))

def gameLoop():  # Boucle principale du jeu
    game_over = False
    game_close = False

    x1 = largeur / 2
    y1 = hauteur / 2

    x1_change = 0
    y1_change = 0

    liste_snake = []
    longueur_snake = 1

    foodx = round(random.randrange(0, largeur - taille_snake) / 10.0) * 10.0
    foody = round(random.randrange(0, hauteur - taille_snake) / 10.0) * 10.0

    while not game_over:

        while game_close:
            fenetre.fill(bleu)
            message("Tu as perdu! Appuie sur Q-Quitter ou C-Continuer", rouge)
            afficher_score(longueur_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -taille_snake
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = taille_snake
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -taille_snake
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = taille_snake
                    x1_change = 0

        if x1 >= largeur or x1 < 0 or y1 >= hauteur or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        fenetre.fill(bleu)

        dessiner_grille()
        pygame.draw.rect(fenetre, vert, [foodx, foody, taille_snake, taille_snake])
        tete_snake = []
        tete_snake.append(x1)
        tete_snake.append(y1)
        liste_snake.append(tete_snake)
        if len(liste_snake) > longueur_snake:
            del liste_snake[0]

        for x in liste_snake[:-1]:
            if x == tete_snake:
                game_close = True

        dessiner_snake(taille_snake, liste_snake)
        afficher_score(longueur_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, largeur - taille_snake) / 10.0) * 10.0
            foody = round(random.randrange(0, hauteur - taille_snake) / 10.0) * 10.0
            longueur_snake += 1

        horloge.tick(vitesse_snake)

    pygame.quit()
    quit()

gameLoop()
