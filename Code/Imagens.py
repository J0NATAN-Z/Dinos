import pygame
import os


#importando as imagens
"""Imagens_passaro = [
        pygame.transform.scale2x(pygame.image.load(os.path.join ("images","berd.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join ("images","berd2.png")))
    ]
Imagens_cactus_big = pygame.transform.scale2x(pygame.image.load(os.path.join ("images","cactusBig0000.png")))
Imagens_cactus_pequeno = pygame.transform.scale2x(pygame.image.load(os.path.join ("images","cactusSmall0000.png")))
Imagens_cactus_pequenoMany = pygame.transform.scale2x(pygame.image.load(os.path.join ("images","cactusSmallMany0000.png")))
Dino_baixo = [
        pygame.transform.scale2x(pygame.image.load(os.path.join ("images","dinoduck0000.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join ("images","dinoduck0001.png")))
]
Dino_corre = [
        pygame.transform.scale2x(pygame.image.load(os.path.join ("images","dinorun0000.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join ("images","dinorun0001.png")))
]

Chao_Nuvens = pygame.transform.scale2x(pygame.image.load(os.path.join ("images","dinoSpritesheet.png")))"""

#importando de outra forma
Imagens_Dino = pygame.image.load(os.path.join("images", "dinoSpritesheet.png"))#.convert_alpha #preseva a transparencia da imagem
print(Imagens_Dino)
