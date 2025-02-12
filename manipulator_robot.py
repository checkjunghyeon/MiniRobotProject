from enums import *
from robot import *

import time
import random

# 조작 가능한 로봇 (ManipulatorRobot)
class ManipulatorRobot(Robot):
    ALLOWED_STATUSES = {
        RobotStatus.IDLE, 
        RobotStatus.Moving, 
        RobotStatus.ERROR, 
        RobotStatus.EMERGENCY_STOP,
        CoBotStatus.PICKING, 
        CoBotStatus.HOLDING, 
        CoBotStatus.PLACING, 
        }  # CHARGING 제외

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
        self.joint_count = joint_count
        self.grasped = False  # 장애물 흡착 여부 (흡착식 gripper 가정)

    def move_joint(self, joint_idx: int, angle: float) -> None: 
        if 0 <= joint_idx < len(self.joint_angles):
            self.joint_angles[joint_idx] = angle
            print(f"       joint[{joint_idx}] moved to {angle}°.")
        else:
            print(f"[ERROR] Invalid joint index {joint_idx}.")

    def calculate_joint_angles(self, x, y, z):
        """ 장애물 위치 (x, y, z) 까지의 관절 이동 각도 계산 """
        angles = [0] * self.joint_count
        for i in range(self.joint_count):
            angles[i] = random.randrange(-180, 180, 10) # -math.pi ~ math.pi

        return angles

    def move_to_obstacle(self, obs_x, obs_y, obs_z):
        """ 장애물 위치 (x, y, z) 까지의 관절 이동 """
        joints = self.calculate_joint_angles(obs_x, obs_y, obs_z)
        for idx, angle in enumerate(joints):
            self.move_joint(idx, angle)

    def grasp_obstacle(self):
        """ 장애물 잡기(흡착) """
        self.grasped = True
        self.log_info(f"Grasping the obstacle.")
        time.sleep(1)

    def lift_obstacle(self):
        """ 장애물 들어 올리기 """
        if self.grasped:  # 장애물 흡착 상태에서만 작동
            self.log_info(f"Grasping the obstacle.")
            for i in random.sample(range(0, self.joint_count), 2):
                self.move_joint(i, 50)  # 무작위로 2개의 관절만 이동
            time.sleep(1)
        else:
            print(f"[ERROR] Nothing to lift.")

    def move_obstacle_to(self, dst_x, dst_y, dst_z):
        self.log_info(f"Moving the obstacle to ({dst_x}, {dst_y}, {dst_z}).")

        joints = self.calculate_joint_angles(dst_x, dst_y, dst_z)
        for idx, angle in enumerate(joints):
            self.move_joint(idx, angle)
        time.sleep(1)

    def release_obstacle(self) -> None:
        """장애물 내려놓기"""
        if self.grasped:  # 장애물 흡착 상태에서만 작동
            self.log_info(f"Releasing the obstacle.")
            self.grasped = False
        else:
            print(f"[ERROR] Nothing to release.")
        time.sleep(1)

    def remove_obstacle(self, obs_pos: list, direction: str) -> None:
        """전체 장애물 제거 과정 순차 실행"""
        x, y, z = obs_pos[0], obs_pos[1], obs_pos[2]
        self.move_to_obstacle(x, y, z)
        self.grasp_obstacle()
        self.lift_obstacle()

        dx = 50 if direction == "left" else -50
        self.move_obstacle_to(x + dx, y, z)
        self.release_obstacle()
        self.log_info(f"{self.name} has cleared the obstacle in the {direction} direction.\n")

    def operate(self, *args) -> None:
        """협동 로봇의 동작: 작업자 지원"""
        if self.power_on:
            self.log_info(f"Assisting mobile robots.")
            self.remove_obstacle(*args)
        else:
            print(f"[ERROR] {self.name} is OFF.")


# 모듈 테스트 코드
if __name__ == "__main__":
    ur10 = Cobot("002", "Cobot-1", "Universal Robots", joint_count=6)
    ur10.power_up()

    ur10.operate(*[10, 20, 30], "left")