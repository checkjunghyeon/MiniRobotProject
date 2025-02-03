from enums import *

# 기본 Robot 클래스
class Robot:
    ALLOWED_STATUSES = {RobotStatus.IDLE, RobotStatus.Moving}  # 기본 허용 상태

    def __init__(self, robot_id: str, name: str, model: str):
        self.robot_id = robot_id
        self.name = name
        self.model = model
        self.status = RobotStatus.IDLE

    def set_status(self, new_status: RobotStatus) -> None:
        """로봇의 상태를 안전하게 변경"""
        if new_status not in self.ALLOWED_STATUSES:
            print(f"[ERROR] {new_status.value} is not a valid status for {self.__class__.__name__}.")
            return
        self.status = new_status
        print(f"{self.name} status changed to {self.status.value}.")

    def operate(self) -> None:
        """기본 로봇은 작업 수행 기능이 없음"""
        print(f"{self.name} has no specific operation.")

    def get_info(self) -> str:
        return f"Robot<{self.robot_id}> [{self.name}] (Model={self.model}), Status={self.status.value}"