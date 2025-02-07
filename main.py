from mobile_robot  import MobileRobot
from manipulator_robot import *
import time

# 순회/감시 로봇 상황 가정
def main():
    amr = MobileRobot("001", "AMR-1", "Jackal")

    print("Initializing AMR-1...")
    print(amr.get_info())
    print("-" * 50)

    print("AMR-1 is starting its patrol...")

    amr.operate(5)

    amr.operate()

if __name__ == "__main__":
    main()