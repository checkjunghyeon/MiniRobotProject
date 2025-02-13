from battery_manager import BatteryManager
from robot import *
from sensor import *
import time
from random import random, sample


def send_alert():
    """ 장애물 감지 시 경고 """
    print(f"\t\t🚨 Beep Beep !! 🚨")
    time.sleep(1)  # 일정 시간 대기


class MobileRobot(Robot):
    ALLOWED_STATUSES = {
        RobotStatus.IDLE, 
        RobotStatus.Moving, 
        RobotStatus.CHARGING,
        RobotStatus.ERROR,
        RobotStatus.EMERGENCY_STOP,
        MobileRobotStatus.OBSTACLE_DETECTED,
        }  # 모든 상태 허용

    def __init__(self, robot_id: str, name: str, model: str, x=0.0, y=0.0, speed=1.0, max_speed=10.0):
        super().__init__(robot_id, name, model)
        self.battery_manager = BatteryManager()  # 배터리 관리 객체 생성
        self.battery = self.battery_manager.get_battery_status()  # 배터리 상태 캐싱

        self.x, self.y, self.speed = x, y, speed
        self.max_speed = max_speed  # 최대 이동 속도 설정

        self.cobot = None # 협동 로봇 연결

        self.sensor = Sensor()
        self.obstacle_detected = False  # 장애물 감지 여부

    def set_cobot(self, cobot):
        """ 협동 로봇 등록 """
        self.cobot = cobot
        print(f"{self.name} is now connected to {cobot.name}.")

    def log_debug(self, message):
        super().log_debug(message)  # 부모 클래스의 log_debug 호출

    def log_info(self, message):
        super().log_info(message)  # 부모 클래스의 log_info 호출
        # 배터리 관리는 개별 로봇에서 하므로 해당 함수에 추가 정보 출력
        print(f"       (Status={self.status} | Battery={self.battery}% | Speed={self.speed} | Pos=({self.x}, {self.y}))")

    def charge(self) -> None:
        self.set_status(RobotStatus.CHARGING)
        time.sleep(1)  # 충전 대기 추가
        self.battery_manager.charge()  # 배터리 충전
        self.set_status(RobotStatus.IDLE)

    def update_battery(self):
        self.battery = self.battery_manager.get_battery_status()

    def move(self, dx: float, dy: float) -> None:
        distance = abs(dx) + abs(dy)
        battery_cost = int((distance * self.speed))  # 속도 요소 추가

        if self.battery < battery_cost:
            print(f"[WARN] {self.name} has insufficient battery ({self.battery}%).")
            return
            
        self.x += dx
        self.y += dy
        self.battery_manager.discharge(battery_cost)  # 배터리 사용
        self.update_battery()
        self.set_status(RobotStatus.Moving)


        self.log_info(f"Moved to ({self.x}, {self.y}) → Battery: -{battery_cost}%")

    def increase_speed(self, n):
        """ 최대 속도(max_speed) 이하로 속도 증가 """
        old_speed = self.speed
        self.speed = min(self.speed + n, self.max_speed)
        self.log_debug(f"Speed increased {old_speed} → {self.speed}")

    def decrease_speed(self, n):
        """ 최저 속도(0) 이상으로 속도 증가 """
        old_speed = self.speed
        self.speed = max(self.speed - n, 0.0)
        self.log_debug(f"Speed decreased {old_speed} → {self.speed}")
        time.sleep(1)

    def patrol_area(self, n_times):
        """ 순찰 기능 """
        print(f"{self.name} is starting its patrol...")
        for _ in range(n_times): # n회 순찰
            dx, dy = sample(range(1, 5), 2)
            self.move(dx, dy)  # 랜덤 위치로 이동

            if self.sensor.detect_obstacle(): # 감지 로직 독립
                self.handle_obstacle()

            if self.battery < 20:
                print("[ALERT] Battery is low, returning to charging station!")
                self.charge()  # 배터리 부족 시 충전
            time.sleep(1)  # 잠시 대기

    def handle_obstacle(self):
        """ 장애물 감지 시 처리 메소드"""
        self.set_status(MobileRobotStatus.OBSTACLE_DETECTED)
        self.obstacle_detected = True
        current_speed = self.speed

        self.log_debug(f"[Warning] Detected an obstacle!")
        self.set_status(RobotStatus.EMERGENCY_STOP)
        self.decrease_speed(current_speed)  # 장애물 감지 시 0으로 감속
        send_alert()  # 장애물 감지 알림

        # 협동 로봇을 통한 장애물 제거
        if self.cobot:
            print(f"\n🚀 Calling {self.cobot.name} for obstacle removal...")
            self.cobot.handle_obstacle([self.x, self.y, 0], "right")  # 장애물 제거 요청
            self.obstacle_detected = False

            # 장애물 제거 후 기존 속도로 복구
            self.set_status(RobotStatus.Moving)
            self.increase_speed(current_speed)
        else:
            print(f"[ERROR] No cobot available for obstacle removal!")

    # OOP 원칙(다형성)을 유지하기 위해 선택적 매개변수 추가
    def operate(self, n_times=None) -> None:
        """이동 로봇의 기본 동작: 이동 및 순찰"""
        self.update_battery()
        if n_times:
            self.patrol_area(n_times)
        else:
            self.log_debug(f"Move to its designated area.")
            dx, dy = sample(range(1, 5), 2)
            self.move(dx, dy)

        self.log_debug(f"Operation completed!")
        self.set_status(RobotStatus.IDLE)

    def get_info(self) -> str:
        return (f"{super().get_info()}, Battery={self.battery}%, "
                f"Speed={self.speed}, Pos=({self.x}, {self.y})")


# 모듈 테스트
if __name__ == "__main__":
    amr = MobileRobot("001", "AMR-1", "Jackal")
    amr.operate(15)
    amr.operate()