from mobile_robot import *
from manipulator_robot import *
from random import sample

def move_n_times(robot, n):
    for _ in range(n):
        dx, dy = sample(range(1, 5), 2)
        robot.move(dx, dy)             # (x + dx, y + dy) 방향으로 이동
        print(robot.get_info())        # 이동 후 위치 및 배터리 확인
        print()

def test_mobile_robot():
    print("===== MobileRobot Test =====\n")

    print('[case 1] 이동 로봇 생성 및 기본 상태 확인')
    robot1 = MobileRobot("001", "AMR-1", "Jackal", x=0.0, y=0.0, speed=1.0)
    print(robot1.get_info())        # 초기 정보 출력
    print()

    print('[case 2] 이동 테스트')
    move_n_times(robot1, 5)

    print('[case 3] 배터리 충전 테스트')
    robot1.charge()  
    robot1.log_info()               # 충전 후 배터리 확인
    print()
    
    print('[case 4] 속도 증감 테스트')
    robot1.increase_speed(5)        # 속도 증가
    move_n_times(robot1, 2)      # 이동

    robot1.decrease_speed(3)        # 속도 증가
    move_n_times(robot1, 2)      # 이동

    print('[case 5] 배터리 부족 시 이동 불가 테스트')
    robot1.battery = 5              # 인위적으로 배터리 부족 상태로 만듦
    robot1.move(3.0, 4.0)    # 이동 시도 -> 실패해야 함
    robot1.log_info()               # 상태 유지 확인
    print()

def test_cobot():
    print("===== Cobot Test =====\n")

    print('[case 1] 협동 로봇 생성 및 초기 정보 확인')
    ur10 = Cobot("002", "Cobot-1", "Universal Robots", joint_count=6)
    ur10.log_info()                 # 기본 정보 출력
    print()
    
    print('[case 2] 관절 이동 테스트')
    ur10.move_joint(3, 30.0)  # 3번 관절을 30도 이동
    ur10.log_info()                 # 이동 후 정보 확인
    print()


if __name__ == "__main__":
    test_mobile_robot()
    # test_cobot()
