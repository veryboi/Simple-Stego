import sys
import pygame
imgfile = "coded.png"
S = pygame.image.load(imgfile)

resolution = S.get_rect().size

pygame.font.init()
systemFont = pygame.font.SysFont('Courier New', 10)
def reset_screen(res):
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("pyview")
    return screen



screen = reset_screen(resolution)
S = S.convert()


def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])
def changeRemainder(n,remainder, base):
    if n % base == remainder:
        return n
    if n - n % base - remainder < 0:
        return n - n % base + remainder
    else:
        return n - n % base - (base-remainder)

def readImg():
    bitTable = []
    readString = ""
    uncompletedBit = ""

    for x in range(resolution[0]):
        for y in range(resolution[1]):
            pixel = S.get_at((x,y))[:3]

            if pixel[2] % 3 == 2:
                for i in range(2):
                    hiddenBit = '{:02b}'.format(S.get_at((x, y))[i] % 4)

                    uncompletedBit = uncompletedBit + hiddenBit
                    if len(uncompletedBit) == 8:
                        bit = '{:08b}'.format(int(uncompletedBit,2))
                        bitTable.append(bit)
                        uncompletedBit = ""

            elif pixel[2] % 3 == 1:
                for i in range(1):
                    hiddenBit = '{:02b}'.format(S.get_at((x, y))[i] % 4)
                    uncompletedBit = uncompletedBit + hiddenBit
                    bit = '{:07b}'.format(uncompletedBit)
                    bitTable.append(bit)
                for i in bitTable:
                    readString = readString + bits2string([i])
                return readString
            else:
                for i in bitTable:
                    readString = readString + bits2string([i])
                return readString
print("yeet")
print(readImg())
print("yeet")
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    screen.blit(S, (0, 0))
    RGB = systemFont.render(str(S.get_at(pygame.mouse.get_pos())[:3]), False, (0,0,0))
    screen.blit(RGB, pygame.mouse.get_pos())
    pygame.display.flip()
    pygame.time.delay(25)
