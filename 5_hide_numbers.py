import pygame
from random import *


def setup(level):  # level에 맞게 리스트 설정
    # 보여줄 숫자 갯수 설정
    number_count = (level//3) + 5
    number_count = min(number_count, 20)

    shuffle_grid(number_count)


def shuffle_grid(number_count):  # 숫자 섞기
    rows = 5
    columns = 9

    cell_size = 130
    button_size = 110
    screen_left_margin = 55
    screen_top_margin = 20

    grid = [[0 for col in range(columns)] for row in range(rows)]

    number = 1
    while number <= number_count:
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            # 현재 그리드 위치 기준으로 좌표 구하기
            center_x = screen_left_margin + (col_idx*cell_size) + (cell_size/2)
            center_y = screen_top_margin + (row_idx*cell_size) + (cell_size/2)

            # 숫자 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)


def display_start_screen():  # 동그라미 그리는 함수
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)


def display_game_screen():  # 게임화면 보여주기
    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            # 버튼 사각형 그리기
            pygame.draw.rect(screen, WHITE, rect)
        else:
            # 숫자 텍스트 그리기
            cell_text = game_font.render(str(idx), True, GRAY)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)


def check_buttons(pos):  # position에 해당하는 버튼확인
    global start
    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True


def check_number_buttons(pos):
    global hidden
    for button in number_buttons:
        if button.collidepoint(pos):  # button에 position이 포함이 되는가?
            if button == number_buttons[0]:
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                print("wrong")
            break


pygame.init()

# 초기 세팅
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("memory game")
game_font = pygame.font.Font(None, 120)

start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height-120)

# 색깔
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

# 숫자가 있는 버튼들
number_buttons = []
# 게임 시작 여부
start = False
# 숫자 숨김 여부
hidden = False

# 게임 시작 전 숫자 설정 함수
setup(1)

# 게임 루프
running = True
while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    screen.fill(BLACK)

    if start:  # 게임 화면 표시
        display_game_screen()
    else:  # 시작 화면 표시
        display_start_screen()

    if click_pos:
        check_buttons(click_pos)

    # 화면 업데이트
    pygame.display.update()

pygame.quit()
