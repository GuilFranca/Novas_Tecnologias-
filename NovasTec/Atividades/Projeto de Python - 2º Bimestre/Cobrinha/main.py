import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# Parâmetros da cobrinha
tamanho_quadrado = 20
velocidade_jogo = 15

# Função para gerar comida
def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y

# Função para desenhar comida
def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

# Função para desenhar a cobrinha
def desenhar_cobra(tamanho_quadrado, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho_quadrado, tamanho_quadrado])

# Função para exibir a pontuação
def exibir_pontuacao(pontuacao):
    fonte = pygame.font.SysFont(None, 35)
    texto = fonte.render("Pontuação: " + str(pontuacao), True, branca)
    tela.blit(texto, [0, 0])

# Função para mostrar o menu inicial
def mostrar_menu():
    menu_ativo = True
    while menu_ativo:
        tela.fill(preta)
        fonte = pygame.font.SysFont(None, 75)
        titulo = fonte.render("Jogo da Cobrinha", True, branca)
        tela.blit(titulo, [largura / 4, altura / 4])
        fonte = pygame.font.SysFont(None, 50)
        instrucoes = fonte.render("Pressione ENTER para Iniciar", True, branca)
        tela.blit(instrucoes, [largura / 4, altura / 2])
        pygame.display.update()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    menu_ativo = False

# Função principal para rodar o jogo
def rodar_jogo():
    fim_jogo = False
    fim_de_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    pixels = []
    comprimento_cobra = 1

    comida_x, comida_y = gerar_comida()
    pontuacao = 0

    while not fim_jogo:

        while fim_de_jogo:
            tela.fill(preta)
            fonte = pygame.font.SysFont(None, 50)
            texto_game_over = fonte.render("Game Over!", True, vermelha)
            texto_instrucao = fonte.render("Q: Sair // C: Jogar Novamente", True, vermelha)
            tela.blit(texto_game_over, [largura / 3, altura / 3])
            tela.blit(texto_instrucao, [largura / 6, altura / 2])
            exibir_pontuacao(pontuacao)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        fim_de_jogo = False
                    if evento.key == pygame.K_c:
                        rodar_jogo()
                        return

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    if velocidade_x == 0:
                        velocidade_x = -tamanho_quadrado
                        velocidade_y = 0
                elif evento.key == pygame.K_RIGHT:
                    if velocidade_x == 0:
                        velocidade_x = tamanho_quadrado
                        velocidade_y = 0
                elif evento.key == pygame.K_UP:
                    if velocidade_y == 0:
                        velocidade_x = 0
                        velocidade_y = -tamanho_quadrado
                elif evento.key == pygame.K_DOWN:
                    if velocidade_y == 0:
                        velocidade_x = 0
                        velocidade_y = tamanho_quadrado

        if x >= largura or x < 0 or y >= altura or y < 0:
            fim_de_jogo = True

        x += velocidade_x
        y += velocidade_y

        tela.fill(preta)
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        cobra_cabeca = []
        cobra_cabeca.append(x)
        cobra_cabeca.append(y)
        pixels.append(cobra_cabeca)
        if len(pixels) > comprimento_cobra:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == cobra_cabeca:
                fim_de_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels)
        exibir_pontuacao(pontuacao)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x, comida_y = gerar_comida()
            comprimento_cobra += 1
            pontuacao += 1

        relogio.tick(velocidade_jogo)

    pygame.quit()
    quit()

relogio = pygame.time.Clock()
mostrar_menu()
rodar_jogo()
