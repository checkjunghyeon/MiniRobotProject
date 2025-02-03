from enums import *
from robot import *

class MobileRobot(Robot):
    ALLOWED_STATUSES = {RobotStatus.IDLE, RobotStatus.Moving, RobotStatus.CHARGING}  # 모든 상태 허용

    def __init__(self, robot_id: str, name: str, model: str, x=0.0, y=0.0, speed=0.0):
        super().__init__(robot_id, name, model)
        self.battery = 100
        self.x, self.y, self.speed = x, y, speed

    def charge(self) -> None:
        self.set_status(RobotStatus.CHARGING)
        self.battery = 100
        print(f"{self.name} is fully charged.")
        self.set_status(RobotStatus.IDLE)

    def move(self, dx: float, dy: float) -> None:
        distance = abs(dx) + abs(dy)
        battery_cost = int(distance * 2)
        if self.battery < battery_cost:
            print(f"[WARN] {self.name} has insufficient battery ({self.battery}%).")
            return
        self.x += dx
        self.y += dy
        self.battery -= battery_cost
        print(f"{self.name} moved to ({self.x}, {self.y}). Battery={self.battery}%")

    def operate(self) -> None:
        """이동 로봇의 기본 동작: 이동"""
        print(f"{self.name} is patrolling its designated area.")

    def get_info(self) -> str:
        return f"{super().get_info()}, Battery={self.battery}%, Speed={self.speed}, Pos=({self.x}, {self.y})"