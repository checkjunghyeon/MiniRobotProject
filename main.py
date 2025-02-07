from mobile_robot  import MobileRobot
from manipulator_robot import *
import time

# 순회/감시 로봇 상황 가정
def main():
    amr = MobileRobot("001", "AMR-1", "Jackal")

    print("Initializing AMR-1...")
    print(amr.get_info())
    print("-" * 50)

    amr.operate(15) # log 독립 후 매개변수(name, message) 손 봐야 함(지금 겁나 꼬임 ㅋㅋ ㅠ)

    amr.operate()  # 단순 이동

if __name__ == "__main__":
    main()