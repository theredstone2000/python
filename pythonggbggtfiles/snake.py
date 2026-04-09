import curses
import random

screen = curses.initcsr()
curses.curs_set(0)
screen.keypad(1)
screen.timeout(100)

sh, sw = screen.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)

snake_x = sw // 4
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]
food = [sh // 2, sw // 2]
w.addch(int(food[0]), int(food[1]), curses.ASC_PI)

key = curses.KEY_RIGHT
directions = {
    'KEY_Z': curses.KEY_UP,
    'KEY_S': curses.KEY_DOWN,
    'KEY_Q': curses.KEY_LEFT,
    'KEY_D': curses.KEY_RIGHT,
}
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if key == directions['KEY_Z']:
        new_head = [snake[0][0] - 1, snake[0][1]]
    elif key == directions['KEY_S']:
        new_head = [snake[0][0] + 1, snake[0][1]]
    elif key == directions['KEY_Q']:
        new_head = [snake[0][0], snake[0][1] - 1]
    elif key == directions['KEY_D']:
        new_head = [snake[0][0], snake[0][1] + 1]

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    if (snake[0][0] in [0, sh] or
        snake[0][1] in [0, sw] or
        snake[0] in snake[1:]):
        curses.endwin()
        quit()

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)