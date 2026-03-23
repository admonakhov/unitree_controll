import sys
import time
from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.g1.loco.g1_loco_client import LocoClient
from gamepad_control import GamePad


class Client(LocoClient):
    def __init__(self):
        super().__init__()
    
    def LockStanding(self):
        self.SetFsmId(4)

    def Walk(self):
        self.SetFsmId(801)

class G1_robot_controller:
    def __init__(self, channel):
        ChannelFactoryInitialize(0, channel)
        self.sport_client = Client()  
        self.sport_client.SetTimeout(10.0)
        self.sport_client.Init()

    def switch_mod(self, btns):
        if ("L2" in btns):
            if ("O" in btns):
                print("DAMPING")
                self.sport_client.Damp()
                
            elif ("UP" in btns):
                print("STAND")
                self.sport_client.LockStanding()
                
            elif ("S" in btns):
                print("WALK")
                self.sport_client.Walk()
    
    def move(self, axis):
        self.sport_client.Move(-axis[1], -axis[0], -axis[2])

        
def run_loop(robot, controller, dt=0.01):
    """
    Fixed timestep loop
    """
    next_time = time.perf_counter()

    while True:
        start = time.perf_counter()
        axis, btns = controller.read_state()
        robot.switch_mod(btns)
        robot.move(axis)

        next_time += dt
        sleep_time = next_time - time.perf_counter()

        if sleep_time > 0:
            time.sleep(sleep_time)
        else:
            next_time = time.perf_counter()



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} networkInterface")
        sys.exit(-1)
    
    controller = GamePad()
    robot = G1_robot_controller(channel=sys.argv[1])
    run_loop(robot, controller, dt=0.02)
    