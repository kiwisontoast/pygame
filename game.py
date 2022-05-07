import pygame,random
WIDTH, HEIGHT=480,800   
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
background=pygame.image.load('space7_4-frames.png')
def main():
    run=True
    while run:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

    pygame.QUIT()

if __name__=="__main__":
    main()
