import pygame


def display_start_screen():  # 동그라미 그리는 함수
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)


def display_game_screen():  # 게임화면 보여주기
    print("game start")


def check_buttons(position):  # position에 해당하는 버튼확인
    global start
    if start_button.collidepoint(position):
        start = True


pygame.init()

# 초기 세팅
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("memory game")

start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height-120)

# 색깔
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 게임 시작 여부
start = False

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
