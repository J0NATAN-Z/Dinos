import pygame
import os
import random
import neat

pygame.init()

ALTURA = 600
LARGURA = 1100
SPEED = 10
ESCOLHENDO = random.choice([0,1])
TELA = pygame.display.set_mode((LARGURA, ALTURA))

RUNNING = [pygame.image.load(os.path.join("Imagens", "DinoRun"+ str(x)+ ".png")).convert_alpha() for x in range (1,3)]

DUCKING = [pygame.image.load(os.path.join("Imagens", "DinoDuck" + str(x) + ".png")).convert_alpha() for x in range(1,3)]

SMALL_CACTUS = [pygame.image.load(os.path.join("Imagens", "SmallCactus"+ str(x) + ".png")).convert_alpha() for x in range(1,4)]

LARGE_CACTUS = [pygame.image.load(os.path.join("Imagens", "LargeCactus"+str(x)+".png")).convert_alpha() for x in range(1,4)]

BIRD = [pygame.image.load(os.path.join("Imagens", "Bird"+str(x)+".png")).convert_alpha() for x in range (1,3)]

CLOUD = pygame.image.load(os.path.join("Imagens", "Cloud.png")).convert_alpha()
GROUND = pygame.image.load(os.path.join("Imagens", "Track.png")).convert_alpha()


class Cloud():
     def __init__(self):
          self.image = CLOUD
          self.rect = self.image.get_rect()
          self.rect.x = LARGURA - random.randint(10,10)
          self.rect.y = random.randint(50,200)
     
     def update(self):
          if self.rect.topright[0] < 0:
               self.rect.x = LARGURA
               self.rect.y = random.randint (50,150)
          self.rect.x -= SPEED

     def draw (self, TELA):
          TELA.blit(self.image, (self.rect.x, self.rect.y))
          
class Cactu():
     def __init__(self):
          self.all_cactus = SMALL_CACTUS + LARGE_CACTUS
          self.imagem_cactus = []
          for imagem in self.all_cactus:
               self.imagem_cactus.append(imagem)
          self.index =0
          self.imagem = self.imagem_cactus[self.index]
          self.rect = self.imagem.get_rect()
          self.rect.x= LARGURA
          self.rect.y = ALTURA - 140
          self.escolha = ESCOLHENDO
          
     def update(self):
          if self.escolha == 0:
               if self.index > 5:
                    self.index =0
               if self.rect.topright[0] < 0:
                    self.rect.x = LARGURA
                    self.index += random.choice(seq=[0,1,2,3,4,5])
                    self.index = self.index % len(self.imagem_cactus)
                    self.imagem = self.imagem_cactus[self.index]
               self.rect.x -= SPEED
          
     def draw(self, TELA):
          TELA.blit(self.imagem,(self.rect.x, self.rect.y))
          
     def get_mask(self):
        return pygame.mask.from_surface(self.imagem)
     
     def width(self):
          return pygame.Surface.get_width(self.imagem)
          
class Bird():
     def __init__(self):
          self.bird = BIRD
          self.imagem_bird = []
          for imagem in self.bird:
               self.imagem_bird.append(imagem)
          self.index =0
          self.imagem = self.imagem_bird[self.index]
          self.rect = self.imagem.get_rect()
          self.rect.x= LARGURA
          self.rect.y = ALTURA - 240
          self.escolha = ESCOLHENDO
          
     def update(self):
          if self.escolha == 1:
               if self.index > 1:
                    self.index =0
               self.index += random.choice(seq=[0,1])
               self.index = self.index % len(self.imagem_bird)
               self.imagem = self.imagem_bird[self.index]
               if self.rect.topright[0] < 0:
                    self.rect.x = LARGURA 
               self.rect.x -=SPEED +1
          
     def draw(self, TELA):
          TELA.blit(self.imagem,(self.rect.x, self.rect.y))
     
     def get_mask(self):
        return pygame.mask.from_surface(self.imagem)

class Ground:
    def __init__(self):
        self.image = GROUND
        self.largura = self.image.get_width()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = ALTURA - 91

    def update(self):
          if self.rect.topright[0] < 1:
               self.rect.x = 0
          self.rect.x -= SPEED

    def draw(self, TELA):
          TELA.blit(self.image, (self.rect.x, self.rect.y))
          TELA.blit(self.image, (self.rect.x + self.largura, self.rect.y))

class Dino():    
     def __init__(self,x,y) :
          self.x = x
          self.y =y
          self.vel = 0
          self.altura = self.y
          self.correndo = RUNNING
          self.dino_imagem = []
          for x in self.correndo:
               self.dino_imagem.append(x)
          self.index = 0 
          self.image = self.dino_imagem[self.index]
          self.drect = self.image.get_rect() #peg o retangulo do da imagem e salva no drect
          self.drect.y = self.y
          self.drect.x = self.x
          
     def jump(self):          
          if self.drect.bottom >= self.y:
            self.vel -= 10
          
     def ducking(self):
          if self.drect.bottom <= self.y:
               self.vel = +12
               
     def update(self):
          if self.index > 1:
               self.index =0
          self.index += 1
          self.index = self.index % len(self.dino_imagem)
          self.image = self.dino_imagem[int(self.index)]
          
          #gravidade
          self.vel += 0.19
          #gravidade+ eixo y da sprite
          self.drect.y += self.vel 
          #verifica a altura da base do sprite
          if self.drect.bottom < 400 :
               #deixa altura trava a 400 ate bottom >= 400
               self.drect.bottom = 400
               #isso é desnecessario
               self.drect.bottom +=0
          #impede que o sprite passe o "chao"
          if self.drect.bottom >= self.y:
            self.drect.bottom = self.y
            self.vel = 0
               
     
     def draw(self,TELA):
          TELA.blit(self.image,self.drect.topleft)
          font = pygame.font.Font(None, 50)
          debug_text = font.render(f"Vel: {self.vel}, Y: {self.drect.bottom}/{self.y}, x: {self.x} ", True, (0, 0, 0))
     
     def get_mask(self):
          return pygame.mask.from_surface(self.image)

class Utilitario:
    def __init__(self):
        self.score = 0
        self.max_score = 0

    def incrementar_score(self):
        global SPEED
        self.score += 1
        if self.score % 100 == 0 and SPEED < 50:
            SPEED += 1

    def atualizar_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score

    def desenhar_scores(self, tela):
        font = pygame.font.Font(None, 50)
        current_score_text = font.render(f"Pontuação: {int(self.score)}", True, (0, 0, 0))
        tela.blit(current_score_text, (800, 20))
        
    @staticmethod
    def verificar_colisao(dino, cactu, bird):
        dino_mask = dino.get_mask()
        cactu_mask = cactu.get_mask()
        bird_mask = bird.get_mask()

        cactu_offset = (cactu.rect.x - dino.drect.x, cactu.rect.y - dino.drect.y)
        bird_offset = (bird.rect.x - dino.drect.x, bird.rect.y - dino.drect.y)

        cactu_colisao = dino_mask.overlap(cactu_mask, cactu_offset)
        bird_colisao = dino_mask.overlap(bird_mask, bird_offset)

        return cactu_colisao or bird_colisao

    def resetar(self, dino, bird, cactu):
          global SPEED,ESCOLHENDO
          self.score = 0
          SPEED = 2
          Utilitario.verificar_colisao 
          ESCOLHENDO = random.choice([0,1])
          bird.rect.x =LARGURA
          cactu.rect.x =LARGURA
          dino.drect.y = 550
                        
def main(genomes, config):
     global ESCOLHENDO
     clock =pygame.time.Clock()
     clock.tick(120)
     run = True
     utilitario = Utilitario()
     cloud= Cloud()
     cactu= Cactu()
     bird = Bird()
     ground = Ground()  
     dinos= []
     nets=[]
     ge= []
          
     for genome_id, genome in genomes:
          genome.fitness = 0  
          net = neat.nn.FeedForwardNetwork.create(genome, config)
          nets.append(net)
          dinos.append(Dino(random.randint(20,70),550))
          ge.append(genome)
     
     while run and len(dinos)> 0:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    run = False
                    break
                         
          #escole "aleatoriamente" qual sprite, cactu e bird, vai ser desenhado
          if cactu.rect.topright[0] <0 or bird.rect.topright[0] <0:
               ESCOLHENDO = random.choice([0,1])
               cactu.rect.x =LARGURA
               cactu.index += random.choice([0,1,2,3,4,5])
               cactu.index = cactu.index % len(cactu.imagem_cactus)
               cactu.imagem = cactu.imagem_cactus[cactu.index]
               cactu.escolha = ESCOLHENDO
               bird.rect.x = LARGURA
               bird.escolha = cactu.escolha
               
          for x, dino in enumerate(dinos):
               ge[x].fitness += 0.15
               #calcula a diferenca entre os objetos e com isso criasse colisao entre elas
               cactu_offset = (cactu.rect.x - dino.drect.x, cactu.rect.y - dino.drect.y)
               bird_offset = (bird.rect.x - dino.drect.x, bird.rect.y - dino.drect.y)
               #são 9 paremetros (inputs) passado pra "IA"
               inputs = ( dino.drect.center[0],dino.drect.center[1],cactu_offset[0],cactu_offset[0] - dino.drect.center[0] ,cactu_offset[1],bird_offset[0], bird_offset[0]- dino.drect.center[0],bird_offset[1], bird_offset[1] - dino.drect.center[1])
               outputs = nets[x].activate(inputs)
               
               #se output < 0.5 corre senao:
               if outputs[0] > 0.5:
                    dino.jump()
               #ou
               if outputs[1] > 0.5:
                    dino.ducking()
          
          for i, dino in enumerate(dinos):
               #se o dino colidir entre os objetos (cactu, bird) a pontuacao daquela geracao sera -1 e logo depois excluida
               if Utilitario.verificar_colisao(dino, cactu, bird):
                    ge[i].fitness -= 1
                    nets.pop(i)
                    ge.pop(i)
                    dinos.pop(i)

          #atualiza os objetos a cada 120 fps
          cloud.update()
          cactu.update()
          bird.update()
          ground.update()
          for dino in dinos:
               dino.update()
               
          #draws on winds      
          TELA.fill((255,255,255))     
          cloud.draw(TELA)
          cactu.draw(TELA)
          bird.draw(TELA)
          ground.draw(TELA)
          dino.draw(TELA)
          
          for dino in dinos:
            dino.draw(TELA)
          utilitario.incrementar_score() 
          utilitario.desenhar_scores(TELA)
          
          pygame.display.update()


def run(config_file):
     config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                              neat.DefaultSpeciesSet, neat.DefaultStagnation,
                              config_file)
     p = neat.Population(config)
     p.add_reporter(neat.StdOutReporter(True))
     stats = neat.StatisticsReporter()
     p.add_reporter(stats)

     #numero de vezes que vai "rodar" ate chegar no objetivo que eh 1500 pontos
     winner = p.run(main, 15)

     # mostra os status final
     print('\nBest genome:\n{!s}'.format(winner))

if __name__ == "__main__":
     local_dir = os.path.dirname(__file__)
     config_path = os.path.join(local_dir, 'config.txt')
     run(config_path)
