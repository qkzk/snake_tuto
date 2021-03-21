'''
title: remake de snake avec pygame zero
'''

import pgzrun
from random import randint

TITLE = "snake"
WIDTH = 400
HEIGHT = 400
CASE = 80
ROW_WIDTH = WIDTH // CASE
COL_HEIGHT = HEIGHT // CASE
BORDER_MARGIN = 5
FRAME_REFRESH = 20


def init_snake() -> list:
    '''Renvoie le serpent initial'''
    return [[3, 0], [2, 0], [1, 0]]


def init_directions() -> list:
    '''Renvoie les directions de départ'''
    return [1, 0]


def draw_snake_element(x: int, y: int, color: str):
    '''Colorie la case (x, y) en `color` '''
    rect = Rect((x * CASE + BORDER_MARGIN, y * CASE + BORDER_MARGIN),
                (CASE - 2 * BORDER_MARGIN, CASE - 2 * BORDER_MARGIN))
    screen.draw.filled_rect(rect, color)


def draw_snake(snake: list):
    '''Dessine le serpent'''
    # dessiner le corps
    for x, y in snake[1:]:
        draw_snake_element(x, y, 'GREEN')
    # dessiner la tête
    x_head, y_head = snake[0]
    draw_snake_element(x_head, y_head, 'ORANGE')


def draw_food(food: list):
    '''dessine la nourriture'''
    x_food, y_food = food
    rect = Rect((x_food * CASE, y_food * CASE), (CASE, CASE))
    screen.draw.filled_rect(rect, 'RED')
    screen.draw.rect(rect, 'WHITE')


def draw_grid():
    '''dessine une grille de carrés blancs à l'écran'''
    for i in range(ROW_WIDTH):
        for j in range(COL_HEIGHT):
            r = Rect((i * CASE, j * CASE), (CASE, CASE))
            screen.draw.rect(r, 'WHITE')


def new_food(snake: list):
    '''
    renvoie une nouvelle position pour la nourriture, qui ne soit pas
    dans le serpent

    On commence par affecter à `new_position` la tête du serpent
    Tant que `new_position` est dans le serpent:
        On choisit une case au hasard dans la grille
        Il suffit de tirer deux entiers entre 0 et `ROW_WIDTH - 1` (inclus)
    On renvoie `new_position`
    '''
    food = snake[0]
    while food in snake:
        food = [randint(0, ROW_WIDTH - 1),
                randint(0, COL_HEIGHT - 1)]
    return food


def check_if_snake_has_eaten(snake: list, food: list) -> bool:
    '''vrai ssi la tete ('snake[0]') est sur la nourriture 'food' '''
    head = snake[0]
    return head == food


def new_head(snake: list, direction: list):
    '''calcule nouvelle position de la tête après déplacement de 'direction' '''
    head = snake[0]
    new_head = [head[0] + direction[0], head[1] + direction[1]]
    return new_head


def move_snake(snake: list, direction: list, has_eaten: list) -> list:
    '''
    déplace le serpent vers direction
    s'il n'a mangé ('has_eaten == False') on efface le dernier élément
    pour le déplacer on ajoute la liste avec [nouvelle tete] au serpent
    précédent
    '''
    if not has_eaten:
        del snake[-1]
    return [new_head(snake, direction)] + snake


def check_death(snake):
    '''
    vrai ssi le serpent meurt
    il meurt s'il sort de l'écran ou si sa tete touche son corps `snake[1:]` '''

    head = snake[0]
    body = snake[1:]
    # s'est-il mordu la queue ?
    if head in body:
        return True

    abs_head = head[0]
    ord_head = head[1]
    # sorti de l'écran ?
    if (
        abs_head < 0 or abs_head >= ROW_WIDTH or
        ord_head < 0 or ord_head >= COL_HEIGHT
    ):
        return True

    # arrivé ici, il n'est pas mort, on renvoie faux
    return False


def reset() -> tuple:
    '''
    Réinitialise les objets globaux.
    Renvoie un triplet (snake, direction, food).
    '''
    snake = init_snake()
    direction = init_directions()
    food = new_food(snake)
    return snake, direction, food


def draw():
    '''
    Appelée 60x par seconde par pygame zero.
    Nettoie l'écran, dessine la grille, la nourriture et le serpent.
    '''
    screen.clear()
    draw_grid()
    draw_food(food)
    draw_snake(snake)


def update():
    '''
    Appelée 60x par seconde par pygame zero.
    Fait tourner le jeu :
    si le compteur de frame est atteint:
        * vérifie si le serpent a mangé et éventuellement calcule une
            nouvelle bouffe,
        * deplace le serpent vers direction,
        * vérifie si le serpent est mort et éventuellement réinitialise
            les objets globaux.
    incrémente le compteur de frames de 1
    '''
    global snake
    global direction
    global food
    global count_frame

    if count_frame >= FRAME_REFRESH:
        has_eaten = check_if_snake_has_eaten(snake, food)
        if has_eaten:
            food = new_food(snake)
        snake = move_snake(snake, direction, has_eaten)
        if check_death(snake):
            snake, direction, food = reset()
        count_frame = 0

    count_frame += 1


def on_key_down(key):
    '''
    Écoute les événements claviers et met à jour un objet
    L'objet `keys` permet de comparer la touche enfoncée `key`
    avec une énumération des touches disponibles

    Les touches de direction sont `keys.LEFT`, `keys.RIGHT` etc.
    '''
    global direction
    if key == keys.ESCAPE:
        exit()
    if key == keys.LEFT:
        direction = [-1, 0]
    if key == keys.RIGHT:
        direction = [1, 0]
    if key == keys.UP:
        direction = [0, -1]
    if key == keys.DOWN:
        direction = [0, 1]


# objets globaux
count_frame = 0
snake = init_snake()
direction = init_directions()
food = new_food(snake)

# lancement du jeu
pgzrun.go()
