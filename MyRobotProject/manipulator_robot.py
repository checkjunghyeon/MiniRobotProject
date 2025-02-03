from enums import *
from robot import *

# 조작 가능한 로봇 (ManipulatorRobot)
class ManipulatorRobot(Robot):
    ALLOWED_STATUSES = {RobotStatus.IDLE, RobotStatus.Moving}  # CHARGING 제외

    def __init__(self, robot_id: str, name: str, model: str):
        super().__init__(robot_id, name, model)
        self.power_on = False

    def power_up(self) -> None:
        self.power_on = True
        print(f"{self.name} power ON.")

    def power_down(self) -> None:
        self.power_on = False
        print(f"{self.name} power OFF.")

    def operate(self) -> None:
        """조작 로봇의 기본 동작: 조립 작업"""
        if self.power_on:
            print(f"{self.name} is assembling components.")
        else:
            print(f"[ERROR] {self.name} is OFF.")

    def get_info(self) -> str:
        return f"{super().get_info()}, PowerOn={self.power_on}"
    
# 협동 로봇 (Cobot)
class Cobot(ManipulatorRobot):
    def __init__(self, robot_id: str, name: str, model: str, joint_count=4):
        super().__init__(robot_id, name, model)
        self.joint_angles = [0.0] * joint_count

    def move_joint(self, joint_idx: int, angle: float) -> None: 
        if 0 <= joint_idx < len(self.joint_angles):
            self.joint_angles[joint_idx] = angle
            print(f"{self.name} joint[{joint_idx}] moved to {angle}°.")
        else:
            print(f"[ERROR] Invalid joint index {joint_idx}.")

    def operate(self) -> None:
        """협동 로봇의 동작: 작업자 지원"""
        if self.power_on:
            print(f"{self.name} assisting human workers.")
        else:
            print(f"[ERROR] {self.name} is OFF.")