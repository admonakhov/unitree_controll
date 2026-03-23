import pygame
import time

class GamePad:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)

        self.btns_map = ["X", 'O', 'T', 'S', 'L1', 'R1', 'L2', 'R2', 'SHARE', 'OPTION', 'PS', 'LT', 'RT']
        self.stick_ax = [0, 1, 3, 4]
        self.threshold = 0.1
        if pygame.joystick.get_count() == 0:
            print("Геймпад не найден")
            pygame.joystick.quit()
            time.sleep(1)
            self.__init__()


    def get_btns(self):
        joystick = self.joystick
        btns = []
        for i in range(joystick.get_numbuttons()):
            if joystick.get_button(i):
                btns.append(self.btns_map[i])
        for i in range(joystick.get_numhats()):
            hat = joystick.get_hat(i)
            if hat == (0, 1):
                btns.append('UP')
            elif hat == (0, -1):
                btns.append('DOWN')
            elif hat == (-1, 0):
                btns.append('LEFT')
            elif hat == (1, 0):
                btns.append('RIGHT')
        return btns
    
    def get_axes(self):
        joystick = self.joystick
        axes = []
        for i in self.stick_ax:
            axes.append(0 if abs(joystick.get_axis(i)) < self.threshold else joystick.get_axis(i))
        return axes
    
    def read_state(self):
        pygame.event.pump()
        btns = self.get_btns()
        axes = self.get_axes()
        return axes, btns



if  __name__ =='__main__':
    controller = GamePad()
    while True:
        print(controller.read_state())
