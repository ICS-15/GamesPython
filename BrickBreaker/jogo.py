import pygame

# inicializar
pygame.init()

## configurar tela de jogo
tamanho_tela = (800,800)
tela = pygame.display.set_mode(tamanho_tela)

## nome jogo
pygame.display.set_caption("Brick Breaker Game")

## variaveis do jogo
tamanho_bola = 15
bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola)

tamanho_jogador = 100
jogador = pygame.Rect(0, 750, tamanho_jogador, tamanho_bola)

qtdade_blocos_linha = 8
qtdade_linha_blocos = 5
qtdade_blocos_totais = qtdade_blocos_linha * qtdade_linha_blocos

def criar_blocos(qtdade_blocos_linha, qtdade_linha_blocos):
    altura_tela = tamanho_tela[1]
    largura_tela = tamanho_tela[0]

    distancia_entre_blocos = 5
    largura_bloco = largura_tela / qtdade_blocos_linha - distancia_entre_blocos
    altura_bloco = 15
    distancia_entre_linhas = altura_bloco + 15

    blocos = []

    for j in range(qtdade_linha_blocos) :
        for i in range(qtdade_blocos_linha) :
            # criar blocos
            bloco = pygame.Rect(i * (largura_bloco + distancia_entre_blocos), j *distancia_entre_linhas, largura_bloco, altura_bloco)
            blocos.append(bloco)

    return blocos

## cores a usar no jogo
cores = {
    "branca" : (255, 255, 255),
    "preta" : (0, 0, 0),
    "amarela" : (255, 255, 0),
    "azul" : (0, 0, 255),
    "verde" : (0, 255, 0)
}

## variaveis gestao do jogo
fim_jogo = False
pontuacao = 0
movimento_bola = [1, -1]


# funções de jogo
def movimentar_jogador(evento):
    if evento.type == pygame.KEYDOWN : 
        if evento.key == pygame.K_RIGHT:
            if jogador.x + tamanho_jogador < tamanho_tela[0] :
                jogador.x += 2.5
        if evento.key == pygame.K_LEFT:
            if jogador.x > 0 :
                jogador.x -= 2.5

def movimentar_bola(bola):
    movimento = movimento_bola
    bola.x += movimento[0]
    bola.y += movimento[1]

    # qd bola bate nos extremos tela
    if bola.x <= 0 :
        movimento[0] = -movimento[0]
    if bola.y <= 0 :
        movimento[1] = -movimento[1]
    if bola.x + tamanho_bola >= tamanho_tela[0] :
        movimento[0] = -movimento[0]
    if bola.y + tamanho_bola >= tamanho_tela[1] :
        movimento = None

    #qd bola bate nos restantes elementos 
    if jogador.collidepoint(bola.x, bola.y) :
        movimento[1] = -movimento[1]
    for bloco in blocos :
        if bloco.collidepoint(bola.x, bola.y) :
            blocos.remove(bloco)
            movimento[1] = -movimento[1]

    return movimento

def atualizar_pontuacao(pontuacao):
    fonte = pygame.font.Font(None,30)
    texto = fonte.render(f"Pontuacao {pontuacao}", 1, cores["amarela"])
    tela.blit(texto,(0, 750))

    if pontuacao >= qtdade_blocos_totais :
        return True
    else : 
        return False
 
# desenhar elementos na tela
def desenhar_inicio_jogo():
    tela.fill(cores["preta"])
    pygame.draw.rect(tela, cores["azul"], jogador)
    pygame.draw.rect(tela, cores["branca"], bola)

def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["verde"], bloco)

## chamar inicio de jogo
blocos = criar_blocos(qtdade_blocos_linha, qtdade_linha_blocos)



# criar loop de jogo
while not fim_jogo :
    # redesenhar a cada iteracao
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)

    fim_jogo = atualizar_pontuacao(qtdade_blocos_totais - len(blocos)) 
    for evento in pygame.event.get() :  
        if evento.type == pygame.QUIT : 
            fim_jogo = True
    movimentar_jogador(evento)

    movimento_bola = movimentar_bola(bola)
    if not movimento_bola :
        fim_jogo = True

    # tempo de espera para correr o loop outra vez
    pygame.time.wait(1)
    # atualiza a tela 
    pygame.display.flip()

## sair do jogo
pygame.quit()