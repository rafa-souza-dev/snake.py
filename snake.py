import pygame
import random

class Frutinha:
    cor = (255, 0, 0)
    tamanho = (10, 10)

    def __init__(self, cobrinha):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        self.posiçao = Frutinha.criar_posiçao(cobrinha)

    def blit(self, screen):
        screen.blit(frutinha.textura, frutinha.posiçao)

    @staticmethod
    def criar_posiçao(cobrinha):
        x = random.randint(0, 49) * 10
        y = random.randint(0, 49) * 10

        if (x, y) in cobrinha.corpo:
            Frutinha.criar_posiçao(cobrinha)
        else:
            return x, y


class Snake:
    cor = (0, 255, 0)
    tamanho = (10, 10)
    velocidade = 10
    tamanho_maximo = 49 * 49

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        self.corpo = [(100, 100), (90, 100), (80, 100)]


        self.direçao = "direita"

        self.pontos = 0

    def blit(self, screen):
        for posiçao in self.corpo:
            screen.blit(self.textura, posiçao)

    def andar(self):
        cabeça = self.corpo[0]
        x = cabeça[0]
        y = cabeça[1]

        if self.direçao == "direita":
            self.corpo.insert(0, (x + self.velocidade, y))
        elif self.direçao == "esquerda":
            self.corpo.insert(0, (x - self.velocidade, y))
        elif self.direçao == "cima":
            self.corpo.insert(0, (x, y - self.velocidade))
        elif self.direçao == "baixo":
            self.corpo.insert(0, (x, y + self.velocidade))

        self.corpo.pop(-1)

    def cima(self):
        if self.direçao != "baixo":
            self.direçao = "cima"

    def baixo(self):
        if self.direçao != "cima":
            self.direçao = "baixo"

    def esquerda(self):
        if self.direçao != "direita":
            self.direçao = "esquerda"

    def direita(self):
        if self.direçao != "esquerda":
            self.direçao = "direita"

    def colisao_frutinha(self, frutinha):
        return self.corpo[0] == frutinha.posiçao

    def comer(self):
        self.corpo.append((0, 0))
        self.pontos += 10
        pygame.display.set_caption(f"RAFIRA SNAKE / pt = {self.pontos}")


    def colisao_parede_corpo(self):
        cabeça = self.corpo[0]
        x = cabeça[0]
        y = cabeça[1]

        return x < 0 or y < 0 or x > 490 or y > 490 or cabeça in self.corpo[1:] or len(self.corpo) > self.tamanho_maximo


if __name__ == "__main__":
    pygame.init()

    resoluçao = (500, 500)
    screen = pygame.display.set_mode(resoluçao)
    clock = pygame.time.Clock()
    preto = (0, 0, 0)

    pygame.display.set_caption("RAFIRA SNAKE")

    cobrinha = Snake()

    frutinha = Frutinha(cobrinha)
    frutinha.blit(screen)


    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cobrinha.cima()
                    break
                elif event.key == pygame.K_DOWN:
                    cobrinha.baixo()
                    break
                elif event.key == pygame.K_LEFT:
                    cobrinha.esquerda()
                    break
                elif event.key == pygame.K_RIGHT:
                    cobrinha.direita()
                    break

        if cobrinha.colisao_frutinha(frutinha):
            cobrinha.comer()
            frutinha = Frutinha(cobrinha)

        if cobrinha.colisao_parede_corpo():
            cobrinha = Snake()

        cobrinha.andar()
        screen.fill(preto)

        frutinha.blit(screen)
        cobrinha.blit(screen)

        pygame.display.update()
