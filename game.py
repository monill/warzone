import pygame as pg

from network import Network

pg.init()
net = Network()

# Declaração de tupla para cores diferentes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
LIGHT_RED = (255, 0, 0)
LIGHT_GREY = (220, 220, 220)
GREEN = (0, 155, 0)
LIGHT_GREEN = (0, 255, 0)

# Cores diferentes para barra de saúde
GREN = (0, 200, 0)
YELOW = (100, 100, 0)
RDE = (200, 0, 0)
YELLOW = (200, 200, 0)
LIGHT_YELLOW = (255, 255, 0)
BLUE = (32, 139, 185)
LIGHT_BLUE = (0, 0, 255)

# Variável para Pausa
PAUSE = False

# Player 1
PLAYER1_DEATH = 0
PLAYER1_KILLS = 0
PLAYER1_STATUS = 'n'  # status (h-hit, d-afogar, n-nenhuma das opções acima)
PLAYER1_BULLET_X = 1285  # player_bullet_x is X coordinate of players bullet
PLAYER1_BULLET_Y = 645  # player_bullet_y is Y coordinate of player's bullet
PLAYER1_HEALTH = 100
PLAYER1_X = 32
PLAYER1_Y = 400

# Player 2
PLAYER2_DEATH = 0
PLAYER2_KILLS = 0
PLAYER2_STATUS = 'n'  # status (h-hit, d-afogar, n-nenhuma das opções acima)
PLAYER2_HEALTH = 100
PLAYER2_X = 1248
PLAYER2_Y = 400

PLAYER2_X_OLD = 1248
PLAYER2_X_CHANGE = 0
PLAYER2_Y_OLD = 400
PLAYER2_Y_CHANGE = 0

PLAYER2_BULLET_X = 1285
PLAYER2_BULLET_Y = 645
PLAYER2_BULLET_OLD = 1285
PLAYER2_BULLET_CHANGE = 0

FONT = pg.font.SysFont('arial', 40, True)

TIME_LEFT = int(300)

# Tamanho da janela
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 640

GAME_DISPLAY = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Background Image
BACKGROUND = pg.image.load("resources/images/misc/background.png")

# Barra de titulo
pg.display.set_caption("Warzone")
ICON = pg.image.load("resources/images/icon.png")
pg.display.set_icon(ICON)

MAIN_MENU = pg.image.load("resources/images/misc/main_menu.png")
GAME_OVER_IMG = pg.image.load("resources/images/misc/game_over.png")
TIMER_BUTTON = pg.image.load("resources/images/misc/timer_button.png")

BULLET_RIGHT = pg.image.load("resources/images/misc/bulletright.png")
BULLET_RIGHT = pg.transform.smoothscale(BULLET_RIGHT, (12, 12))
BULLET_LEFT = pg.transform.flip(BULLET_RIGHT, True, False)

walking = {
    1: pg.image.load("resources/images/walk/1.png"),
    2: pg.image.load("resources/images/walk/2.png"),
    3: pg.image.load("resources/images/walk/3.png"),
    4: pg.image.load("resources/images/walk/4.png"),
    5: pg.image.load("resources/images/walk/5.png"),
    6: pg.image.load("resources/images/walk/6.png"),
    7: pg.image.load("resources/images/walk/7.png"),
    8: pg.image.load("resources/images/walk/8.png")
}

walk_right = [
    walking[1],
    walking[2],
    walking[3],
    walking[4],
    walking[5],
    walking[6],
    walking[7],
    walking[8]
]

walk_left = [
    pg.transform.flip(walking[1], True, False),
    pg.transform.flip(walking[2], True, False),
    pg.transform.flip(walking[3], True, False),
    pg.transform.flip(walking[4], True, False),
    pg.transform.flip(walking[5], True, False),
    pg.transform.flip(walking[6], True, False),
    pg.transform.flip(walking[7], True, False),
    pg.transform.flip(walking[8], True, False)
]

dying = {
    1: pg.image.load("resources/images/dead/1.png"),
    2: pg.image.load("resources/images/dead/2.png"),
    3: pg.image.load("resources/images/dead/3.png"),
    4: pg.image.load("resources/images/dead/4.png"),
    5: pg.image.load("resources/images/dead/5.png"),
    6: pg.image.load("resources/images/dead/6.png"),
    7: pg.image.load("resources/images/dead/7.png"),
    8: pg.image.load("resources/images/dead/8.png")
}

dead_right = [
    dying[1],
    dying[2],
    dying[3],
    dying[4],
    dying[5],
    dying[6],
    dying[7],
    dying[8]
]

dead_left = [
    dying[1],
    dying[2],
    dying[3],
    dying[4],
    dying[5],
    dying[6],
    dying[7],
    dying[8]
]

# Variáveis do ID da animação == 0
WALK_P1 = 0
LEFT_P1 = False
RIGHT_P1 = False
JUMP_P1 = False
STAND_RIGHT_P1 = True
STAND_LEFT_P1 = False

# Variáveis para o ID da animação == 1
WALK_P2 = 0
LEFT_P2 = False
RIGHT_P2 = False
JUMP_P2 = False
STAND_RIGHT_P2 = False
STAND_LEFT_P2 = True

pg.display.update()
FPS = 30
DEATH = 0
clock = pg.time.Clock()

# Tamanhos de fonte diferentes
FONT_SMALL = pg.font.SysFont("arial", 25)
FONT_MEDIUM = pg.font.SysFont("arial", 50)
FONT_LARGE = pg.font.SysFont("arial", 80)

CHAT_STR = ""
PRINT_CHAT = ""
PRINT_CHAT_CHECK = ""
CHAT_WORD = ""
FPS_COUNT = 0
TIME_STR = ""
PREV = ""
START_TICK = 0
TIMER_COUNT = 0
TIMER_FLAG = 0

AIR = False  # Jogador no ar ou não

# Inicial para id == 1
if net.id == "1":
    PLAYER1_X = 1248
    PLAYER1_Y = 400
    PLAYER2_X = 32
    PLAYER2_Y = 400


# Função para exibir algumas mensagens na tela
def message_to_screen(message, color, displace_y=0, size="small"):
    text_surf, text_rect = text_objects(message, color, size)
    text_rect.center = (640, 200 + displace_y)
    GAME_DISPLAY.blit(text_surf, text_rect)


# para limpar o texto impresso na tela após 5 segundos
# Atualiza a tela a cada instante para que o jogo continue funcionando sem remover os dados necessários da tela
def chat_screen_update():
    GAME_DISPLAY.fill(WHITE)
    GAME_DISPLAY.blit(BACKGROUND, [0, 0])
    button("Chat", 1180, 11, 90, 40, YELLOW, LIGHT_YELLOW)
    button("Pausa", 1180, 55, 90, 40, RED, LIGHT_RED, action="paused")
    GAME_DISPLAY.blit(TIMER_BUTTON, [580, 10])
    text = FONT_SMALL.render(CHAT_WORD + PRINT_CHAT, True, BLACK)
    GAME_DISPLAY.blit(text, [20, 60])
    text_button(TIME_STR, BLACK, 623, 24, 30, 30)
    health_bars(PLAYER1_HEALTH, PLAYER2_HEALTH)  # desenhar barras de saúde
    player_draw(PLAYER1_X, PLAYER1_Y, ICON)  # desenha jogador 1
    player_draw(PLAYER2_X, PLAYER2_Y, ICON, True)  # desenha jogador 2

    # imagem de bala de acordo com a direção
    if PLAYER2_BULLET_CHANGE > 0:
        GAME_DISPLAY.blit(BULLET_RIGHT, (PLAYER2_BULLET_X, PLAYER2_BULLET_Y))
    else:
        GAME_DISPLAY.blit(BULLET_LEFT, (PLAYER2_BULLET_X, PLAYER2_BULLET_Y))


# Cria objetos de texto de acordo com o tamanho especificado
def text_objects(message, color, size="small"):
    # A instrução abaixo foi adicionada apenas para evitar a variável local de erro usada antes da referência
    text_surface = FONT_SMALL.render(message, True, color)
    if size == "small":
        text_surface = FONT_SMALL.render(message, True, color)
    elif size == "medium":
        text_surface = FONT_MEDIUM.render(message, True, color)
    elif size == "large":
        text_surface = FONT_LARGE.render(message, True, color)

    return text_surface, text_surface.get_rect()


# Adiciona texto aos botões
def text_button(message, color, button_x, button_y, button_width, button_height, size="small"):
    text_surf, text_rect = text_objects(message, color, size)
    text_rect.center = ((button_x + (button_width // 2)), (button_y + (button_height // 2)))
    GAME_DISPLAY.blit(text_surf, text_rect)


# Regras e regulamentos, juntamente com controles.
def helps():
    while True:
        GAME_DISPLAY.fill(GREEN)
        message_to_screen("AJUDA", RED, -100, "large")
        message_to_screen("Disparar e matar o inimigo", BLACK, 0, "small")
        message_to_screen("PRESSIONE BARRA DE ESPAÇO PARA DISPARAR", BLACK, 60, "small")
        message_to_screen(
            "AS BARRAS DE SAÚDE MANTÊM CONSTANTEMENTE UM CONTROLE DA SUA SAÚDE, BEM COMO A SAÚDE DO SEU INIMIGO", BLACK,
            120, "small")
        message_to_screen(
            "A PONTUAÇÃO NO CANTO SUPERIOR ESQUERDO SIGNIFICA A RELAÇÃO DO JOGADOR 1 MATA A JOGADOR 2 MATA", BLACK, 180,
            "small")
        message_to_screen("PRESSIONE O BOTÃO CHAT PARA ENVIAR UMA MENSAGEM", BLACK, 240, "small")
        message_to_screen("PRESSIONE O BOTÃO DE PAUSA PARA PAUSAR A TELA", BLACK, 280, "small")

        # Retorna a tupla da posição do mouse na tela
        cur = pg.mouse.get_pos()
        # Retorna uma tupla na qual o botão do mouse é pressionado, se esquerda ou direita, por exemplo
        # (1, 0, 0) significa que a esquerda foi pressionada
        click = pg.mouse.get_pressed()

        # Para clarear o botão quando o mouse estiver sobre ele
        if 130 + 150 > cur[0] > 130 and 535 + 50 > cur[1] > 535:
            pg.draw.rect(GAME_DISPLAY, LIGHT_RED, (130, 535, 150, 50))
            # que está no clique esquerdo
            if click[0] == 1:
                game_intro()
        else:
            pg.draw.rect(GAME_DISPLAY, YELLOW, (885, 535, 150, 50))

        # colocar texto no botão
        text_button("Voltar", BLACK, 130, 535, 150, 50)
        text_button("Play", BLACK, 885, 535, 150, 50)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        clock.tick(15)


# Cria botões.
def button(text, x, y, width, height, inactive_color, active_color, action=None):
    # para adicionar funcionalidade ao botão
    global PAUSE
    cur = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    # click possui tupla contendo 3 elementos. primeiro clique esquerdo, segundo mouse, terceiro clique direito

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pg.draw.rect(GAME_DISPLAY, active_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            if action == "quit":
                pg.quit()
                quit()
            if action == "chat":
                chat_box()
            if action == "paused":
                PAUSE = True
                paused()
            if action == "unpause":
                unpause()
        else:
            pg.draw.rect(GAME_DISPLAY, inactive_color, (x, y, width, height))
            text_button(text, BLACK, x, y, width, height)


# Esta função é chamada sempre que o botão de bate-papo é pressionado e exibe o texto como tipo u.
def chat_box():
    global CHAT_WORD, PRINT_CHAT, CHAT_STR

    chat_screen_update()
    pg.display.update()

    PRINT_CHAT = ""
    current_string = []
    output = ""
    writing = True

    while writing:
        CHAT_WORD = "Chat:"
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    current_string = current_string[0:-1]
                elif event.key == pg.K_RETURN:
                    writing = False
                    break
                elif event.key == pg.K_MINUS:
                    current_string.append("_")
                elif event.key <= 127:
                    current_string.append(chr(event.key))

        output = "".join(current_string)
        text = FONT_SMALL.render(CHAT_WORD + output, True, BLACK)
        timer(START_TICK)
        chat_screen_update()
        GAME_DISPLAY.blit(text, [20, 60])
        pg.display.update()

    CHAT_STR = output


# Permite que o bate-papo seja exibido por 5 segundos.
def chatting():
    global CHAT_STR, PRINT_CHAT, PRINT_CHAT_CHECK, FPS_COUNT, CHAT_WORD

    reply = send_data(CHAT_STR)

    if reply != PRINT_CHAT_CHECK:
        PRINT_CHAT = reply
        FPS_COUNT = 0

    if FPS_COUNT <= 151:
        FPS_COUNT += 1

    if len(PRINT_CHAT) > 0 and FPS_COUNT == 1:
        CHAT_WORD = "Chat:"
        text = FONT_SMALL.render(CHAT_WORD + PRINT_CHAT, True, BLACK)
        # print_chat_check = PRINT_CHAT

        GAME_DISPLAY.blit(text, [20, 60])
        pg.display.update()


# Envia dados para o servidor via arquivo de rede.
def send_data(output):
    global PLAYER1_X, PLAYER1_Y, PLAYER1_BULLET_X, PLAYER1_BULLET_Y, PLAYER1_STATUS
    global PLAYER2_X, PLAYER2_Y, PLAYER2_BULLET_X, PLAYER2_BULLET_Y, PLAYER2_STATUS
    global TIMER_COUNT, CHAT_WORD
    global PLAYER2_Y_OLD, PLAYER2_Y_CHANGE, PLAYER2_X_OLD, PLAYER2_X_CHANGE, PLAYER2_BULLET_CHANGE, PLAYER2_BULLET_OLD

    data = str(net.id) + ":" + output + '?' + str(PLAYER1_X) + ',' + str(PLAYER1_Y) + ',' + str(
        PLAYER1_BULLET_X) + ',' + str(PLAYER1_BULLET_Y) + ',' + str(PLAYER1_STATUS)
    reply = net.send(data)
    arr = reply.split('?')
    TIMER_COUNT = int(arr[3])
    print(reply)
    if net.id == "0":
        PLAYER2_X = int(arr[2][2:].split(',')[0])
        PLAYER2_Y = int(arr[2][2:].split(',')[1])
        PLAYER2_BULLET_X = int(arr[2][2:].split(',')[2])
        PLAYER2_BULLET_Y = int(arr[2][2:].split(',')[3])
        PLAYER2_STATUS = (arr[2][2:].split(',')[4])
        PLAYER1_X = int(arr[1][2:].split(',')[0])
        PLAYER1_Y = int(arr[1][2:].split(',')[1])
        PLAYER1_BULLET_X = int(arr[1][2:].split(',')[2])
        PLAYER1_BULLET_Y = int(arr[1][2:].split(',')[3])
        PLAYER1_STATUS = (arr[1][2:].split(',')[4])
    else:
        PLAYER2_X = int(arr[1][2:].split(',')[0])
        PLAYER2_Y = int(arr[1][2:].split(',')[1])
        PLAYER2_BULLET_X = int(arr[1][2:].split(',')[2])
        PLAYER2_BULLET_Y = int(arr[1][2:].split(',')[3])
        PLAYER2_STATUS = (arr[1][2:].split(',')[4])
        PLAYER1_X = int(arr[2][2:].split(',')[0])
        PLAYER1_Y = int(arr[2][2:].split(',')[1])
        PLAYER1_BULLET_X = int(arr[2][2:].split(',')[2])
        PLAYER1_BULLET_Y = int(arr[2][2:].split(',')[3])
        PLAYER1_STATUS = (arr[2][2:].split(',')[4])

    # Para direção do inimigo e sua bala
    PLAYER2_X_CHANGE = PLAYER2_X - PLAYER2_X_OLD
    PLAYER2_Y_CHANGE = PLAYER2_Y - PLAYER2_Y_OLD
    PLAYER2_X_OLD = PLAYER2_X
    PLAYER2_Y_OLD = PLAYER2_Y
    PLAYER2_BULLET_CHANGE = PLAYER2_BULLET_X - PLAYER2_BULLET_OLD
    PLAYER2_BULLET_OLD = PLAYER2_BULLET_X

    reply = arr[0]

    return reply[2:]


# Cancela a "pausa" do jogo
def unpause():
    global PAUSE
    PAUSE = False


# Pausa o jogo
def paused():
    global START_TICK

    text_surf, text_rect = text_objects("Pausado", RED, "large")
    text_rect.center = (630, 200)
    GAME_DISPLAY.blit(text_surf, text_rect)
    time_add = 0

    while PAUSE:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        button("Continue", 300, 372, 150, 50, RED, LIGHT_RED, action="unpause")
        button("Quit", 842, 372, 150, 50, BLUE, LIGHT_BLUE, action="quit")

        pg.display.update()
        clock.tick(15)
    else:
        chat_screen_update()


# Exibe Game Over Screen.
def game_over():
    global PLAYER1_DEATH, PLAYER1_KILLS
    global PLAYER2_DEATH, PLAYER2_KILLS
    global TIMER_COUNT, CHAT_STR, PRINT_CHAT, PRINT_CHAT_CHECK, FPS_COUNT, CHAT_WORD

    pg.mixer.music.stop()
    pg.mixer.music.load("resources/sounds/game_over.mp3")
    pg.mixer.music.play(-1)

    CHAT_STR = ""
    PRINT_CHAT = ""
    PRINT_CHAT_CHECK = ""
    FPS_COUNT = 0
    CHAT_WORD = ""
    game_over = True
    start_time = pg.time.get_ticks()
    flag = 1

    while game_over:
        time_left = 4 - (pg.time.get_ticks() - start_time) / 1000
        if time_left > 0 and flag == 1:
            send_data("")

            if TIMER_COUNT == 0:
                flag = 0

        GAME_DISPLAY.fill(WHITE)
        GAME_DISPLAY.blit(GAME_OVER_IMG, [0, 0])

        if int(PLAYER1_DEATH) < int(PLAYER2_DEATH):
            text_surf, text_rect = text_objects("Voce Ganhou", RED, "large")
            text_rect.center = (957, 177)
            GAME_DISPLAY.blit(text_surf, text_rect)

            text_surf1, text_rect1 = text_objects(
                "Player 1: " + " + " + str(PLAYER1_KILLS) + "   - " + str(PLAYER1_DEATH), BLACK, "small")
            text_rect1.center = (957, 277)
            GAME_DISPLAY.blit(text_surf1, text_rect1)

            text_surf2, text_rect2 = text_objects(
                "Player 2: " + " + " + str(PLAYER2_KILLS) + "   - " + str(PLAYER2_DEATH), BLACK, "small")
            text_rect2.center = (957, 327)
            GAME_DISPLAY.blit(text_surf2, text_rect2)

        elif int(PLAYER1_DEATH) > int(PLAYER2_DEATH):

            text_surf, text_rect = text_objects("Voce Perdeu", RED, "large")
            text_rect.center = (957, 177)
            GAME_DISPLAY.blit(text_surf, text_rect)

            text_surf1, text_rect1 = text_objects(
                "Player 1: " + " + " + str(PLAYER1_KILLS) + "   - " + str(PLAYER1_DEATH), BLACK, "small")
            text_rect1.center = (957, 277)
            GAME_DISPLAY.blit(text_surf1, text_rect1)

            text_surf2, text_rect2 = text_objects(
                "Player 2: " + " + " + str(PLAYER2_KILLS) + "   - " + str(PLAYER2_DEATH), BLACK, "small")
            text_rect2.center = (957, 327)
            GAME_DISPLAY.blit(text_surf2, text_rect2)
        else:
            text_surf, text_rect = text_objects("Empate", RED, "large")
            text_rect.center = (957, 177)
            GAME_DISPLAY.blit(text_surf, text_rect)

            text_surf1, text_rect1 = text_objects(
                "Player 1 :" + " + " + str(PLAYER1_KILLS) + "   - " + str(PLAYER1_DEATH), BLACK, "small")
            text_rect1.center = (957, 277)
            GAME_DISPLAY.blit(text_surf1, text_rect1)

            text_surf2, text_rect2 = text_objects(
                "PLAYER 2 :" + " + " + str(PLAYER2_KILLS) + "   - " + str(PLAYER2_DEATH), BLACK, "small")
            text_rect2.center = (957, 327)
            GAME_DISPLAY.blit(text_surf2, text_rect2)

        # retorna a tupla da posição do mouse na tela
        cur = pg.mouse.get_pos()
        # retorna uma tupla na qual o botão do mouse é pressionado, se esquerda ou direita, por exemplo:
        # (1,0,0) significa que a esquerda foi pressionada
        click = pg.mouse.get_pressed()

        if 770 + 170 > cur[0] > 770 and 560 + 50 > cur[1] > 560:
            # para clarear o botão quando o mouse estiver sobre ele
            pg.draw.rect(GAME_DISPLAY, LIGHT_RED, (770, 560, 170, 50))

            if click[0] == 1:
                PLAYER2_KILLS = 0
                PLAYER2_DEATH = 0
                PLAYER1_DEATH = 0
                PLAYER1_KILLS = 0

                game_loop()

            else:
                pg.draw.rect(GAME_DISPLAY, RED, (770, 560, 170, 50))

            if 1010 + 170 > cur[0] > 1010 and 560 + 50 > cur[1] > 560:
                pg.draw.rect(GAME_DISPLAY, LIGHT_YELLOW, (1010, 560, 170, 50))

                if click[0] == 1:
                    pg.quit()
                    quit()
                else:
                    pg.draw.rect(GAME_DISPLAY, YELLOW, (1010, 560, 170, 50))

                # para colocar o texto no botão
                text_button("Jogar novamente", BLACK, 770, 560, 170, 50)
                text_button("Quit", BLACK, 1010, 560, 170, 50)

                pg.display.update()
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()

                clock.tick(10)


# Exibe a tela de introdução do jogo.
def game_intro():
    pg.mixer.music.load("resources/sounds/menu_sound.mp3")
    pg.mixer.music.play(-1)

    while True:
        GAME_DISPLAY.fill(WHITE)
        GAME_DISPLAY.blit(MAIN_MENU, [0, 0])

        # retorna a tupla da posição do mouse na tela
        cur = pg.mouse.get_pos()
        # retorna uma tupla na qual o botão do mouse é pressionado, no centro esquerdo ou direito, por exemplo:
        # (1,0,0) significa que o botão esquerdo é pressionado
        click = pg.mouse.get_pressed()

        if 842 + 150 > cur[0] > 842 and 291 + 50 > cur[1] > 291:
            # para clarear o botão quando o mouse estiver sobre ele
            pg.draw.rect(GAME_DISPLAY, LIGHT_RED, (842, 291, 150, 50))

            if click[0] == 1:
                game_loop()
            else:
                pg.draw.rect(GAME_DISPLAY, RED, (842, 291, 150, 50))

        if 842 + 150 > cur[0] > 842 and 372 + 50 > cur[1] > 372:
            pg.draw.rect(GAME_DISPLAY, LIGHT_YELLOW, (842, 372, 150, 50))

            if click[0] == 1:
                helps()
            else:
                pg.draw.rect(GAME_DISPLAY, YELLOW, (842, 372, 150, 50))

        if 842 + 150 > cur[0] > 842 and 456 + 50 > cur[1] > 456:
            pg.draw.rect(GAME_DISPLAY, LIGHT_BLUE, (842, 456, 150, 50))

            if click[0] == 1:
                pg.quit()
                quit()
            else:
                pg.draw.rect(GAME_DISPLAY, BLUE, (842, 456, 150, 50))

        text_button("Jogar", BLACK, 842, 291, 150, 50)
        text_button("Help", BLACK, 842, 372, 150, 50)
        text_button("Quit", BLACK, 842, 456, 150, 50)

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        clock.tick(10)


# Permite que o chat seja exibido durante o jogo e não interrompa o jogo.
def chat_with_player():
    global CHAT_STR, PRINT_CHAT, PRINT_CHAT_CHECK, FPS_COUNT, CHAT_WORD

    if FPS_COUNT == 150:
        CHAT_STR = ""
        PRINT_CHAT = ""
        CHAT_WORD = ""
        chat_screen_update()


# Game Timer
def timer(start_tick):
    global TIME_LEFT, TIMER_COUNT, TIME_STR, PREV

    if TIMER_COUNT < 2:
        if TIME_LEFT > 300:
            text_surf, text_rect = text_objects("Esperando que o(a) outro(a) jogador(a) se conecte...", RED, "small")
            text_rect.center = (630, 150)
            GAME_DISPLAY.blit(text_surf, text_rect)
            clock.tick(300)

    pg.display.update()

    time_left = 301 - (pg.time.get_ticks() - start_tick) / 1000
    min, sec = divmod(time_left, 60)

    if int(min) == int(0) and int(sec) == int(0):
        game_over()

    if sec < 10:
        sec = '0' + str(int(sec))
    else:
        sec = str(int(sec))

    time_str = "0" + str(int(min)) + ":" + sec
    if time_str != PREV:
        GAME_DISPLAY.blit(TIMER_BUTTON, [580, 10])
        text_button(time_str, BLACK, 623, 24, 30, 30, "medium")

    PREV = time_str


# Movimento do jogador com id = 0 e id = 1 respectivamente
def player_draw(player_x, player_y, image, mirror=False):
    global WALK_P1, LEFT_P1, RIGHT_P1, STAND_RIGHT_P1, STAND_LEFT_P1
    global WALK_P2, LEFT_P2, RIGHT_P2, STAND_RIGHT_P2, STAND_LEFT_P2

    player_x -= 16
    if net.id == '1':
        mirror = not mirror
    if mirror:
        image = pg.transform.flip(image, True, False)
    if net.id == '1':  # display score
        text = FONT.render('Pontos  ' + str(PLAYER1_DEATH) + " : " + str(PLAYER1_KILLS), 1, (0, 0, 0))
    else:
        text = FONT.render('Pontos  ' + str(PLAYER1_KILLS) + " : " + str(PLAYER1_DEATH), 1, (0, 0, 0))
    GAME_DISPLAY.blit(text, (10, 20))
    if net.id != '1':
        if not mirror:
            if WALK_P1 + 1 >= 32:
                WALK_P1 = 0
            if LEFT_P1:
                GAME_DISPLAY.blit(walk_left[WALK_P1 // 4], [player_x, player_y])
                WALK_P1 += 1
                LEFT_P1 = False
                STAND_LEFT_P1 = True
                STAND_RIGHT_P1 = False
            elif RIGHT_P1:
                GAME_DISPLAY.blit(walk_right[WALK_P1 // 4], [player_x, player_y])
                WALK_P1 += 1
                RIGHT_P1 = False
                STAND_RIGHT_P1 = True
                STAND_LEFT_P1 = False
            elif STAND_RIGHT_P1:
                GAME_DISPLAY.blit(image, [player_x, player_y])
            elif STAND_LEFT_P1:
                # image = pg.transform.flip(image, True, False)
                GAME_DISPLAY.blit(image, [player_x, player_y])
        else:
            if WALK_P2 + 1 >= 32:
                WALK_P2 = 0
            elif PLAYER2_X_CHANGE > 0:
                GAME_DISPLAY.blit(walk_right[WALK_P2 // 4], [player_x, player_y])
                WALK_P2 += 1
                RIGHT_P2 = False
                STAND_LEFT_P2 = False
                STAND_RIGHT_P2 = True
            elif PLAYER2_X_CHANGE < 0:
                GAME_DISPLAY.blit(walk_left[WALK_P2 // 4], [player_x, player_y])
                WALK_P2 += 1
                LEFT_P2 = False
                STAND_LEFT_P2 = True
                STAND_RIGHT_P2 = False
            elif STAND_RIGHT_P2:
                GAME_DISPLAY.blit(image, [player_x, player_y])
            elif STAND_LEFT_P2:
                # image = pygame.transform.flip(image, True, False)
                GAME_DISPLAY.blit(image, [player_x, player_y])
    else:
        if mirror:
            if WALK_P2 + 1 >= 32:
                WALK_P2 = 0
            if LEFT_P2:
                GAME_DISPLAY.blit(walk_left[WALK_P2 // 4], [player_x, player_y])
                WALK_P2 += 1
                LEFT_P2 = False
                STAND_LEFT_P2 = True
                STAND_RIGHT_P2 = False
            elif RIGHT_P2:
                GAME_DISPLAY.blit(walk_right[WALK_P2 // 4], [player_x, player_y])
                WALK_P2 += 1
                RIGHT_P2 = False
                STAND_RIGHT_P2 = True
                STAND_LEFT_P2 = False
            elif STAND_RIGHT_P2:
                GAME_DISPLAY.blit(image, [player_x, player_y])
            elif STAND_LEFT_P2:
                # image = pg.transform.flip(image, True, False)
                GAME_DISPLAY.blit(image, [player_x, player_y])
        else:
            if WALK_P1 + 1 >= 32:
                WALK_P1 = 0
            if PLAYER2_X_CHANGE < 0:
                GAME_DISPLAY.blit(walk_left[WALK_P1 // 4], [player_x, player_y])
                WALK_P1 += 1
                LEFT_P1 = False
                STAND_LEFT_P1 = True
                STAND_RIGHT_P1 = False
            elif PLAYER2_X_CHANGE > 0:
                GAME_DISPLAY.blit(walk_right[WALK_P1 // 4], [player_x, player_y])
                WALK_P1 += 1
                RIGHT_P1 = False
                STAND_RIGHT_P1 = True
                STAND_LEFT_P1 = False
            elif STAND_RIGHT_P1:
                GAME_DISPLAY.blit(image, [player_x, player_y])
            elif STAND_LEFT_P1:
                # image = pg.transform.flip(image, True, False)
                GAME_DISPLAY.blit(image, [player_x, player_y])


# Para verificar se o jogador / bala está tentando se sobrepor a um obstáculo
def obstacle_check(player_x, player_y, change_x, change_y, air_stay, direction, obstacle_x, obstacle_y, width, height,
                   player_width=28, player_height=60):
    global AIR

    if obstacle_x <= player_x + change_x <= obstacle_x + width or obstacle_x <= player_x + player_width + change_x <= obstacle_x + width:
        if obstacle_y <= player_y + change_y <= obstacle_y + height or obstacle_y <= player_y + player_height + change_y <= obstacle_y + height or player_y <= obstacle_y < player_y + player_height or player_y <= obstacle_y + height <= player_y + player_height:

            if player_width == 24 and player_height == 24:  # for fire
                air_stay = True
                return change_x, change_y, air_stay, direction
            if direction["right"] and direction["up"] == 0 and direction["down"] == 0:
                change_x = obstacle_x - player_x - player_width
            elif direction["left"] and direction["up"] == 0 and direction["down"] == 0:
                change_x -= obstacle_x + width - player_x
            elif direction["up"] == 0 and direction["down"] == 0:
                if abs(obstacle_x - player_x - player_width) < abs(obstacle_x + width - player_x):
                    change_x = obstacle_x - player_x - player_width
                else:
                    change_x = obstacle_x + width - player_x
            if direction["up"]:
                if obstacle_y < player_y + change_y < obstacle_y + height:
                    change_y = + 8
                    direction["up"] = 0
                    direction["down"] = 1
                    air_stay = 32 - air_stay - 2
                if air_stay != 0:
                    change_x = 0
            elif direction["down"]:
                if obstacle_y < player_y + player_height + change_y < obstacle_y + height or obstacle_y < player_y + change_y < obstacle_y + height:
                    change_y = obstacle_y - player_y - player_height
                    if change_y < 0:
                        change_y = +16
                    direction["up"] = 0
                    direction["down"] = 0
                    air_stay = 0
                    AIR = False
                if air_stay != 0:
                    change_x = 0

    return change_x, change_y, air_stay, direction


# Solicita verificação de obstáculos() para todos os obstáculos/oponente
def obstacles(playerX, playerY, x_change, y_change, air_stay_count, direction, player_width=28, player_height=60):
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 128, 352, 32, 32, player_width,
                                                                   player_height)  # plank 2
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 0, 480, 512, 32, player_width,
                                                                   player_height)  # ground 1
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 0, 512, 480, 32, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 0, 544, 448, 32, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 0, 576, 416, 32, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 0, 608, 384, 32, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 224, 288, 192, 32, player_width,
                                                                   player_height)  # plank 3
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 256, 320, 128, 64, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 0, 224, 96, 64, player_width,
                                                                   player_height)  # plank 1
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 0, 192, 128, 32, player_width,
                                                                   player_height)  # plank 1
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 0, 288, 64, 32, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 0, 320, 32, 32, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 544, 224, 128, 96, player_width,
                                                                   player_height)  # plank 4
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 800, 256, 128, 96, player_width,
                                                                   player_height)  # plank 5
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 640, 480, 192, 32, player_width,
                                                                   player_height)  # ground 2
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 672, 512, 128, 64, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 704, 576, 64, 32, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 960, 480, 320, 32, player_width,
                                                                   player_height)  # ground 3
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 992, 512, 288, 32, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 1024, 544, 256, 32, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 1056, 576, 224, 32, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 1088, 608, 192, 32, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 1120, 352, 32, 32, player_width,
                                                                   player_height)  # plank 7
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 1056, 256, 32, 32, player_width,
                                                                   player_height)  # plank 6
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 1152, 192, 128, 32, player_width,
                                                                   player_height)  # plank 8
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 1184, 224, 96, 64, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 1216, 288, 64, 32, player_width,
                                                                   player_height)
    x_change, y_change, air_stay_count, direction = obstacle_check(playerX, playerY, x_change, y_change, air_stay_count,
                                                                   direction, 1248, 320, 32, 32, player_width,
                                                                   player_height)

    return x_change, y_change, air_stay_count, direction


# Atualizar os medidores de saúde mostrando indicação de saúde com cores diferentes
def health_bars(player_health, player2_health):
    if player_health > 75:
        player_health_color = GREN
    elif player_health > 50:
        player_health_color = YELOW
    else:
        player_health_color = RDE

    if player2_health > 75:
        player2_health_color = GREN
    elif player2_health > 50:
        player2_health_color = YELOW
    else:
        player2_health_color = RDE
    if net.id == '0':
        pg.draw.rect(GAME_DISPLAY, player_health_color, (430, 25, player_health, 30))
        pg.draw.rect(GAME_DISPLAY, player2_health_color, (750, 25, player2_health, 30))
    else:
        pg.draw.rect(GAME_DISPLAY, player_health_color, (750, 25, player_health, 30))
        pg.draw.rect(GAME_DISPLAY, player2_health_color, (430, 25, player2_health, 30))


# Disparar balas
def fire(playerY, face, move_fire, direc):
    global PLAYER1_BULLET_Y

    fire_bullet = True
    if face == "left":
        direc["left"] = 1
        move_fire -= 16
        if move_fire < 0:
            fire_bullet = False
        X, Y, air, direc = obstacles(move_fire, PLAYER1_BULLET_Y, -16, 0, 0, direc, 24, 24)
        if air:
            fire_bullet = False
        else:
            GAME_DISPLAY.blit(BULLET_LEFT, [move_fire, PLAYER1_BULLET_Y])
    else:
        direc["right"] = 1
        move_fire += 16
        if move_fire > 1280:
            fire_bullet = False
        X, Y, air, direc = obstacles(move_fire, PLAYER1_BULLET_Y, 16, 0, 0, direc, 24, 24)
        if air:
            fire_bullet = False
        else:
            GAME_DISPLAY.blit(BULLET_RIGHT, [move_fire, PLAYER1_BULLET_Y])

    return fire_bullet, move_fire


# Função principal do jogo que chama todas as outras funções de acordo com o requisito para tornar o jogo funcional.
def game_loop():
    # para poder modificar a direção
    global LEFT_P1, LEFT_P2
    global RIGHT_P1, RIGHT_P2
    global JUMP_P1, JUMP_P2
    global PAUSE, DEATH

    global PLAYER1_HEALTH, PLAYER1_KILLS, PLAYER1_DEATH
    global PLAYER2_HEALTH, PLAYER2_KILLS, PLAYER2_DEATH

    global PLAYER1_X, PLAYER1_Y
    global PLAYER2_X, PLAYER2_Y

    global PLAYER1_BULLET_X, PLAYER1_BULLET_Y
    global PLAYER2_BULLET_X, PLAYER2_BULLET_Y

    global START_TICK, PLAYER1_STATUS, PLAYER2_STATUS, AIR

    pg.mixer.music.stop()
    pg.mixer.music.load("resources/sounds/music.mp3")
    pg.mixer.music.play(-1)

    # Manipulação de eventos
    GAME_DISPLAY.fill(WHITE)
    GAME_DISPLAY.blit(BACKGROUND, [0, 0])
    game_exit = False

    PLAYER1_HEALTH = 100
    PLAYER2_HEALTH = 100

    direction = {"right": 0, "left": 0, "up": 0, "down": 0}

    PLAYER1_X = 32
    PLAYER1_Y = 400
    PLAYER2_X = 1248
    PLAYER2_Y = 400

    if net.id == "1":
        PLAYER1_X = 1248
        PLAYER1_Y = 400
        PLAYER2_X = 32
        PLAYER2_Y = 400

    air_stay_count = 0  # variável para manter o jogador no ar
    x_change = 0
    y_change = 0
    face = "left"  # Jogador direção está virado

    # Atirando
    fire_x = 1285  # Bala coordenada x
    fire_y = 685  # Bala coordenada y
    fire_bullet = False  # Bala é disparada ou não
    direc_fire = {"left": 0, "right": 0, "up": 0, "down": 0}
    direc_fire_const = direc_fire
    face_const = face

    START_TICK = pg.time.get_ticks()

    temp_air = False

    status_count = 0
    player2_status_count = 0

    while not game_exit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_exit = True

        keys = pg.key.get_pressed()
        if TIMER_COUNT == 2:
            if keys[pg.K_UP] and air_stay_count == 0 and direction["down"] == 0 and AIR == False:
                jump = True
                direction["up"] = 1
                air_stay_count = 38
                AIR = True

            if keys[pg.K_LEFT]:
                if net.id != "1":
                    LEFT_P1 = True
                    RIGHT_P1 = False
                    JUMP_P1 = False
                elif net.id == "1":
                    LEFT_P2 = True
                    RIGHT_P2 = False
                    JUMP_P2 = False

                x_change = -4
                face = "left"
                direction["left"] = 1
                direction["right"] = 0

            if keys[pg.K_RIGHT]:
                if net.id != "1":
                    LEFT_P1 = False
                    RIGHT_P1 = True
                    JUMP_P1 = False
                elif net.id == "1":
                    LEFT_P2 = False
                    RIGHT_P2 = True
                    JUMP_P2 = False

                x_change = +4
                face = "right"
                direction["left"] = 0
                direction["right"] = 1

            if keys[pg.K_SPACE] and fire_bullet == False and PLAYER1_STATUS == "n":
                fire_x = PLAYER1_X
                fire_y = PLAYER1_Y
                fire_bullet = True
                direc_fire_const = direc_fire
                face_const = face
                PLAYER1_BULLET_X = fire_x
                PLAYER1_BULLET_Y = PLAYER1_Y + 12

            if keys[pg.K_p]:
                pg.draw.rect(GAME_DISPLAY, RED, (1180, 55, 90, 40))
                PAUSE = True
                paused()

        button("Chat", 1180, 11, 90, 40, YELLOW, LIGHT_YELLOW, action="chat")
        button("Pausa", 1180, 55, 90, 40, RED, LIGHT_RED, action="paused")

        if TIMER_COUNT < 2:
            START_TICK = pg.time.get_ticks()
        timer(START_TICK)

        if air_stay_count > 19:  # para permanecer no ar/loop
            air_stay_count -= 1
            y_change = -8
            direction["up"] = 1
            direction["down"] = 0
        elif air_stay_count <= 19:
            air_stay_count -= 1
            y_change = +8
            direction["down"] = 1
            direction["up"] = 0

        chatting()
        chat_with_player()

        if PLAYER1_STATUS != "n" and status_count != 1:  # alterar status do jogador
            PLAYER1_STATUS = "n"
            status_count = 0
        elif PLAYER1_STATUS != "n" and status_count == 1:
            status_count += 1

        if PLAYER1_Y + y_change >= 520:  # condições de contorno
            air_stay_count = 0
            y_change = 0
            PLAYER1_Y = 576
            PLAYER1_HEALTH = 0
            AIR = False
            x_change = 0
            PLAYER1_STATUS = "d"
            status_count += 1
        elif PLAYER1_Y + y_change <= 0:
            y_change = +8
            direction["up"] = 0
            direction["down"] = 1
            air_stay_count = 32 - air_stay_count - 2

        if PLAYER1_X + x_change <= 0:
            x_change = 0
            PLAYER1_X = 0
        elif PLAYER1_X + x_change + 32 >= 1280:
            x_change = 0
            PLAYER1_X = 1280 - 32

        if PLAYER1_HEALTH != 0:  # verifique os obstáculos para o jogador
            x_change, y_change, air_stay_count, direction = obstacles(PLAYER1_X, PLAYER1_Y, x_change, y_change,
                                                                      air_stay_count, direction)

        PLAYER1_X += x_change
        PLAYER1_Y += y_change
        x_change = 0
        y_change = 0
        direction["down"] = 0
        direction["up"] = 0
        direction["right"] = 0
        direction["left"] = 0

        chat_screen_update()

        if fire_bullet:
            if temp_air:
                fire_bullet = False
                PLAYER1_BULLET_X = 1285
                PLAYER1_BULLET_Y = 645
                PLAYER1_STATUS = 'h'
                PLAYER2_HEALTH -= 10
                temp_air = False
                status_count += 1
            else:
                fire_bullet, fire_x = fire(fire_y, face_const, fire_x, direc_fire_const)
                PLAYER1_BULLET_X = fire_x

                if face_const == "left":  # verifique os obstáculos para obter marcadores
                    player_1_2_x, player_1_2_y, temp_air, temp_dict = obstacle_check(PLAYER1_BULLET_X, PLAYER1_BULLET_Y,
                                                                                     -16, 0, 0, direc_fire_const,
                                                                                     PLAYER2_X, PLAYER2_Y, 32, 32, 24,
                                                                                     24)

                else:
                    player_1_2_x, player_1_2_y, temp_air, temp_dict = obstacle_check(PLAYER1_BULLET_X, PLAYER1_BULLET_Y,
                                                                                     16, 0, 0,
                                                                                     direc_fire_const, PLAYER2_X,
                                                                                     PLAYER2_Y, 32, 32, 24, 24)

        else:
            PLAYER1_BULLET_X = 1285
            PLAYER1_BULLET_Y = 645

        if PLAYER2_STATUS == 'd':  # changes according to enemy status
            if player2_status_count == 0:
                PLAYER2_HEALTH = 0
                player2_status_count += 1
        elif PLAYER2_STATUS == 'h':
            if player2_status_count == 0:
                PLAYER1_HEALTH -= 10
                player2_status_count += 1
        elif PLAYER2_STATUS == 'n':
            player2_status_count = 0

        if PLAYER2_HEALTH == 0:
            if net.id == "0":
                if RIGHT_P2:
                    if DEATH + 1 >= 32:
                        DEATH = 0
                    GAME_DISPLAY.blit(dead_right[DEATH // 4], [PLAYER2_X, PLAYER2_Y])
                    DEATH += 1
                else:
                    if DEATH + 1 >= 32:
                        DEATH = 0
                    GAME_DISPLAY.blit(dead_left[DEATH // 4], [PLAYER2_X, PLAYER2_Y])
                    DEATH += 1
            if net.id == "1":
                if RIGHT_P1:
                    if DEATH + 1 >= 32:
                        DEATH = 0
                    GAME_DISPLAY.blit(dead_right[DEATH // 4], [PLAYER2_X, PLAYER2_Y])
                    DEATH += 1
                else:
                    if DEATH + 1 >= 32:
                        DEATH = 0
                    GAME_DISPLAY.blit(dead_left[DEATH // 4], [PLAYER2_X, PLAYER2_Y])
                    DEATH += 1
            PLAYER1_KILLS += 1
            PLAYER2_DEATH += 1
            PLAYER2_HEALTH = 100
            if net.id == '1':
                PLAYER2_X = 32
                PLAYER2_Y = 400
            else:
                PLAYER2_X = 1248
                PLAYER2_Y = 400

        if PLAYER1_HEALTH == 0:
            if net.id == "0":
                if RIGHT_P1:
                    if DEATH + 1 >= 32:
                        DEATH = 0
                    GAME_DISPLAY.blit(dead_right[DEATH // 4], [PLAYER1_X, PLAYER1_Y])
                    DEATH += 1
                else:
                    if DEATH + 1 >= 32:
                        DEATH = 0
                    GAME_DISPLAY.blit(dead_left[DEATH // 4], [PLAYER1_X, PLAYER1_Y])
                    DEATH += 1
            if net.id == "1":
                if RIGHT_P2:
                    if DEATH + 1 >= 32:
                        DEATH = 0
                    GAME_DISPLAY.blit(dead_right[DEATH // 4], [PLAYER1_X, PLAYER1_Y])
                    DEATH += 1
                else:
                    if DEATH + 1 >= 32:
                        DEATH = 0
                    GAME_DISPLAY.blit(dead_left[DEATH // 4], [PLAYER1_X, PLAYER1_Y])
                    DEATH += 1
            PLAYER1_DEATH += 1
            PLAYER1_KILLS += 1
            PLAYER1_HEALTH = 100
            if net.id == '0':
                PLAYER1_X = 32
                PLAYER1_Y = 400
            else:
                PLAYER1_X = 1248
                PLAYER1_Y = 400

        pg.display.update()

        clock.tick(FPS)

    pg.quit()
    quit()


game_intro()
