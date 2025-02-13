# 🦾 Mobile & Cobot Robot Simulation

## 📌 프로젝트 개요
이 프로젝트는 **이동 로봇(Mobile Robot)과 협동 로봇(Cobot)이 협력하여 장애물을 감지하고 제거하는 시뮬레이션**입니다.
이동 로봇은 장애물을 감지하면 정지하고, 협동 로봇을 호출하여 장애물을 제거한 후 다시 이동합니다.
또한, 배터리 관리를 수행하며, 배터리가 부족하면 자동으로 충전소로 이동합니다.

## ✨ 주요 기능
### 🚗 이동 로봇 (MobileRobot)
- **장애물 감지** → `sensor.detect_obstacle()`
- **장애물 감지 시 정지 및 협동 로봇 호출** → `handle_obstacle()`
- **배터리 관리** → `BatteryManager`
- **순찰 및 이동** → `patrol_area(n_times)`, `move(dx, dy)`

### 🤖 협동 로봇 (Cobot)
- **장애물 제거 기능** → `handle_obstacle(position, direction)`


## 🚀 실행 방법
```sh
python main.py
```

## 📝 사용 예제
```python
from mobile_robot import MobileRobot
from manipulator_robot import Cobot

# 로봇 객체 생성
amr = MobileRobot("001", "AMR-1", "Jackal")
ur10 = Cobot("002", "Cobot-1", "Universal Robots", joint_count=6)

# 협동 로봇 연결
amr.set_cobot(ur10)

# 이동 로봇 작동
amr.operate(5)  # 5회 순찰
amr.operate()  # 랜덤 이동
```

## 📂 프로젝트 구조
```
📦 robot-simulation
├── 📄 main.py              # 메인 실행 파일
├── 📄 robot.py             # 기본 로봇 클래스
├── 📄 mobile_robot.py      # 이동 로봇
├── 📄 manipulator_robot.py # 협동 로봇
├── 📄 sensor.py            # 장애물 감지 센서
├── 📄 battery_manager.py   # 배터리 관리
├── 📄 logger.py            # 로그 출력 관리
├── 📄 enums.py             # 로봇 상태 관리
└── 📄 README.md            # 프로젝트 설명 문서
```

## 📌 추가 기능 및 개선점
- 장애물의 개수 및 위치를 랜덤하게 생성하는 기능 추가 가능
- RGB 및 Depth 카메라 센서 연결 확장
- 로봇 간 통신을 네트워크 기반으로 확장 가능
