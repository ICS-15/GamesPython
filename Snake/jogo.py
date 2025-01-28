
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

cores_cobra = {
    "azul": (0, 0, 255),
    "amarelo": (255, 255, 0),
    "ciano": (0, 255, 255),
    "laranja": (255, 165, 0),
    "branca" : (255, 255, 255)
}

## parametros para a cobra
tamanho_quadrado = 20
velocidade_jogo = 10

def criar_comida():
    ## usar round para alinhamento de itens 
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return   comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, cores["verde"], [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels, cor_cobra):
    for pixel in pixels:
        pygame.draw.rect(tela, cor_cobra, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, cores["vermelha"])
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla, ultima_direcao, velocidade_x, velocidade_y):
    if (tecla == pygame.K_s or tecla == pygame.K_DOWN) and ultima_direcao != 'UP':
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
        nova_direcao ='DOWN'
    elif (tecla == pygame.K_w or tecla == pygame.K_UP) and ultima_direcao != 'DOWN':
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
        nova_direcao = 'UP'
    elif (tecla == pygame.K_d or tecla == pygame.K_RIGHT) and ultima_direcao != 'LEFT':
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
        nova_direcao = 'RIGTH'
    elif (tecla == pygame.K_a or tecla == pygame.K_LEFT) and ultima_direcao != 'RIGTH':
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
        nova_direcao = 'LEFT'
    else:
        # Caso qualquer outra tecla seja pressionada, não muda a direção
        velocidade_x = velocidade_x
        velocidade_y = velocidade_y
        nova_direcao = ultima_direcao
    return velocidade_x, velocidade_y, nova_direcao

def desenhar_tela_intro():
    tela.fill(cores["preta"])
    fonte = pygame.font.Font(None, 50)
    texto_inicio = fonte.render("Snake", True, cores["branca"])
    texto_instrucao = pygame.font.Font(None, 30).render("Pressione qualquer tecla para iniciar", True, cores["branca"])
    texto_instrucao_2 = pygame.font.Font(None, 30).render("Utilize as setas ou as teclas a w d s para jogar", True, cores["branca"])


    # Centralizando o texto
    tela.blit(texto_inicio, (largura // 2 - texto_inicio.get_width() // 2, 100))
    tela.blit(texto_instrucao, (largura // 2 - texto_instrucao.get_width() // 2, 200))
    tela.blit(texto_instrucao_2, (largura // 2 - texto_instrucao_2.get_width() // 2, 250))

    pygame.display.flip()

# Tela de introdução
def mostrar_intro():
    intro_ativa = True

    while intro_ativa:
        desenhar_tela_intro()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                intro_ativa = False
            if evento.type == pygame.KEYDOWN:
                #if evento.key == pygame.K_SPACE:
                    intro_ativa = False  # Sai da tela de introdução
                    correr_jogo()

    pygame.time.wait(1)

def correr_jogo():
    ## variaveis de inicio de jogo
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = tamanho_quadrado
    velocidade_y = 0

    tamanho_cobra = 1
    ## permite o crescimento da cobra
    pixels = []
    comida_x, comida_y =  criar_comida()
    ultima_direcao = 'RIGHT'
    cor_cobra = random.choice(list(cores_cobra.values()))
    cor_alterada = False
    nova_cor_cobra = cor_cobra
    velocidade_jogo = 10
    
    ## criar loop infinito
    while not fim_jogo :

        tela.fill(cores["preta"])

        for evento in pygame.event.get() :
            if evento.type == pygame.QUIT : 
                fim_jogo = True 
            elif evento.type == pygame.KEYDOWN :
                velocidade_x, velocidade_y, ultima_direcao = selecionar_velocidade(evento.key, ultima_direcao, velocidade_x, velocidade_y)  

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

        desenhar_cobra(tamanho_quadrado, pixels,cor_cobra)

        ## pontuacao
        desenhar_pontuacao(tamanho_cobra -1)
        if (tamanho_cobra -1) % 5 == 0 and tamanho_cobra != 1 and not cor_alterada:
            while cor_cobra == nova_cor_cobra : 
                nova_cor_cobra = random.choice(list(cores_cobra.values()))
                velocidade_jogo += 2
            cor_cobra = nova_cor_cobra
            cor_alterada = True

        if (tamanho_cobra-1) % 5 != 0:
            cor_alterada = False

        ## atualizar tela
        pygame.display.update()

        ## criar nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = criar_comida()

        if fim_jogo :
            mostrar_intro()
        relogio.tick(velocidade_jogo)
mostrar_intro()
