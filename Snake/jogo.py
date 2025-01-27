
#configuracoes iniciais
import pygame
import random

## inicializar pygame
pygame.init()

## inicializar tela
pygame.display.set_caption("Snake game")
largura, altura = 1200, 600
tela = pygame.display.set_mode((largura, altura))

relogio = pygame.time.Clock()

## cores a usar no jogo 
cores = {
    "branca" : (255, 255, 255),
    "preta" : (0, 0, 0),
    "vermelha" : (255, 0, 0),
    "verde" : (0, 255, 0)
}

## parametros para a cobra
tamanho_quadrado = 20
velocidade_jogo = 15

def criar_comida():
    ## usar round para alinhamento de itens 
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return   comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, cores["verde"], [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, cores["branca"], [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, cores["vermelha"])
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def correr_jogo():
    ## variaveis de inicio de jogo
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    ## permite o crescimento da cobra
    pixels = []
    comida_x, comida_y =  criar_comida()

    ## criar loop infinito
    while not fim_jogo :

        tela.fill(cores["preta"])

        for evento in pygame.event.get() :
            if evento.type == pygame.QUIT : 
                fim_jogo = True 
            elif evento.type == pygame.KEYDOWN :
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)  

        ## atualizar cobra
        x += velocidade_x
        y += velocidade_y

        ## cobra bate na parede
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        # desenhar objetos na tela
        ## comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        ## cobra
        pixels.append([x,y])
        ## movimento cobra
        if len(pixels) > tamanho_cobra:
            del pixels[0] 

        ## cobra bate nela mesma 
        for pixel in pixels[:-1] :
            if pixel == [x, y] :
                fim_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels)

        ## pontuacao
        desenhar_pontuacao(tamanho_cobra -1)

        ## atualizar tela
        pygame.display.update()

        ## criar nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = criar_comida()

        relogio.tick(velocidade_jogo)

correr_jogo()