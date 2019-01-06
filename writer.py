import sys
import pygame
resolution = (1000,600)
pygame.font.init()
systemFont = pygame.font.SysFont('Courier New', 10)
def reset_screen(res):
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("pyview")
    return screen


imgfile = "mountains.jpg"


S = pygame.image.load(imgfile)
S=pygame.transform.scale(S, resolution)
screen = reset_screen(resolution)
S = S.convert()
MAX_VALUE = 255


def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]


def changeRemainder(n,remainder, base):
    if n % base == remainder:
        return n
    if n - n % base - remainder < 0:
        return n - n % base + remainder
    else:
        return n - n % base - (base-remainder)


def writeImg(text):
    print("Characters per image: " + str(resolution[0] * resolution[1] // 2 + 1))
    print("You have " + str(len(text)) + " characters.")
    if resolution[0] * resolution[1] // 2 + 1 < len(text):
        print("!ERROR!")
        sys.exit()

    index = 0
    byteIndex = 0
    text = text.replace('\n', ' ').replace('\r', '')
    bits = string2bits(text)
    bitsLength = len(bits)
    for x in range(resolution[0]):
        for y in range(resolution[1]):

            orgColor = S.get_at((x, y))[:3]
            newColor = list(orgColor)
            # 'r' will be encoded
            for i in range(2):
                if index + 1 <= bitsLength:
                    currentBits = bits[index][byteIndex:byteIndex+2]
                    #000000xx

                    newColor[i] = changeRemainder(orgColor[i], int(currentBits, 2), 4)
                    byteIndex += 2
                    if byteIndex == 8:
                        byteIndex = 0
                        index += 1
                else:
                    for v in range(len(newColor)):
                        if newColor[v] > MAX_VALUE:
                            newColor[v] = MAX_VALUE
                        elif newColor[v] < 0:
                            newColor[v] = 0
                    if i == 0:

                        newColor[2] = changeRemainder(newColor[2], 0,3)
                        S.set_at((x, y), newColor)

                        return
                    else:
                        newColor[2] = changeRemainder(newColor[2], 1,3)
                        S.set_at((x, y), newColor)

                        return
            newColor[2] = changeRemainder(newColor[2], 2,3)

            for i in range(len(newColor)):
                if newColor[i] > MAX_VALUE:
                    newColor[i] = MAX_VALUE
                elif newColor[i] < 0:
                    newColor[i] = 0
            S.set_at((x, y), newColor)



    screen.blit(S, (0, 0))


x= ''
print(r'What would you like to encrypt? After entering your to-be-encrypted text, press enter, then type "done", '
      r'then press enter again, for this program to hide your text.')
done = False
while not done:
    inputx = input()
    if inputx == "done":
        break

    x = x + inputx
pygame.init()
writeImg(x)


takenImage = False
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    screen.blit(S, (0, 0))
    RGB = systemFont.render(str(S.get_at(pygame.mouse.get_pos())[:3]), False, (0,0,0))
    screen.blit(RGB, pygame.mouse.get_pos())
    pygame.display.flip()
    pygame.time.delay(25)
    if not takenImage:
        print("image has been saved")
        pygame.image.save(screen, "coded.png")
        takenImage = True
