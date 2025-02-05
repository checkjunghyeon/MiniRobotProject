from enum import Enum

class RobotStatus(Enum):
    IDLE = "Idle"
    Moving = "Moving"
    CHARGING = "Charging"
    ERROR = "Error"                          # 오류 발생
    EMERGENCY_STOP = "Emergency Stop"        # 비상 정지
    
# 주행 로봇
class MobileRobotStatus(Enum):
    OBSTACLE_DETECTED = "Obstacle Detected"  # 장애물 탐지

# 협동 로봇
class CoBotStatus(Enum):
    PICKING = "Picking"                      # 물건 집기
    HOLDING = "Holding"                      # 집고있는 상태
    PLACING = "Placing"                      # 물건 내려놓기

from enum import Enum

class RobotStatus(Enum):
    IDLE = "Idle"
    Moving = "Moving"
    CHARGING = "Charging"
    ERROR = "Error"                          # 오류 발생
    EMERGENCY_STOP = "Emergency Stop"        # 비상 정지
    
# 주행 로봇
class MobileRobotStatus(Enum):
    OBSTACLE_DETECTED = "Obstacle Detected"  # 장애물 탐지

# 협동 로봇
class CoBotStatus(Enum):
    PICKING = "Picking"                      # 물건 집기
    HOLDING = "Holding"                      # 집고있는 상태
    PLACING = "Placing"                      # 물건 내려놓기
