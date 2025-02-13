from mobile_robot  import MobileRobot
from manipulator_robot import *
import time

def initialize(robot):
    print(f"Initializing {robot.name}...")
    print(robot.get_info())
    print("-" * 50)

# 순회/감시 로봇 상황 가정
def main():
    amr = MobileRobot("001", "AMR-1", "Jackal")
    ur10 = Cobot("002", "Cobot-1", "Universal Robots", joint_count=6)

    initialize(amr)
    initialize(ur10)

    amr.set_cobot(ur10)
    amr.operate(10)  # n회 순찰

    amr.operate()  # 단순 이동

if __name__ == "__main__":
    main()