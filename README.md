## 🫡 프로젝트 목적
- 파이썬 기초 및 심화 문법 학습 🐍
- 객체 지향 프로그래밍(OOP) 원칙 이해 및 적용


## 📌 프로젝트 개요 (**순찰 시뮬레이션**)

- **이동 로봇(Mobile Robot)과 협동 로봇(Cobot)이** 협력하여 **장애물을 감지하고 제거하는** 시뮬레이션
- **시뮬레이션 프로세스 (Simulation Process)**
    - 이동 로봇(mobile robot)이 정해진 횟수만큼 이동하며 순찰(patrol)
    - 이동 중 **장애물을 감지하면 정지**하고, 협동 로봇(cobot)을 호출하여 **장애물을 제거**
    - 장애물이 제거되면 순찰 재개
    - 이동 시 배터리가 부족하면 자동으로 충전소로 이동

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
├── 📄 enums.py             # 로봇 동작 상태 정의
└── 📄 README.md            # 프로젝트 설명 문서

```

## ✨ 주요 기능


### 🚗 이동 로봇 (MobileRobot)

- **장애물 감지** → `sensor.detect_obstacle()`
- **장애물 감지 시 정지 및 협동 로봇 호출** → `handle_obstacle()`
- **배터리 관리** → `BatteryManager`
- **순찰 및 이동** → `patrol_area(n_times)`, `move(dx, dy)`

### 🤖 협동 로봇 (Cobot)

- **장애물 제거 기능** → `handle_obstacle(position, direction)`

## 🚀 실행 방법

```
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

---


## **1️⃣ 기능적 변화 (기존 vs 수정 후로 양식 변경 필요)**


### ✅ **장애물 감지 및 처리 기능 추가**

🔹 `sensor.detect_obstacle()`을 통해 **장애물 감지**

🔹 `handle_obstacle()`을 통해 **협동 로봇 호출 및 장애물 제거**

### ✅ **협동 로봇과의 협업 강화**

🔹 `Cobot` 클래스 도입 → **이동 로봇이 협동 로봇을 호출하여 장애물을 제거하도록 변경**

🔹 `set_cobot()` 메서드를 추가하여 **협동 로봇을 이동 로봇과 연결 가능**

### ✅ **배터리 관리 기능 추가**

🔹 `BatteryManager` 클래스를 도입하여 **배터리 상태를 체크하고 자동 충전**

🔹 배터리가 부족하면 충전소로 이동

## **2️⃣ OOP 확장 요소**

### 🔹 **클래스 간 책임 분리**

| 기존 예제 | 개선 후 |
| --- | --- |
| `MobileRobot`이 모든 기능 담당 | **역할별 클래스 분리** |
| 장애물 감지 & 제거 기능 없음 | `Sensor`, `Cobot`, `BatteryManager` 추가 |

### 🔹 **객체 간 협력 관계 추가**

🔹 `MobileRobot` → `Cobot`, `Sensor`, `BatteryManager` **구성(Composition) 활용**

### 🔹 **다형성 적용**

🔹 `operate(n_times=None)` → **선택적 매개변수로 유연한 이동 & 순찰 가능**


### 🅰️ 객체 지향의 4대 원칙

- **🔹 캡슐화**
    
    ✅ MobileRobot, Cobot 내부에서도 속성을 직접 수정하는 대신 메서드를 통해 데이터를 관리
    
    ✅ BatteryManager에서 배터리 상태를 직접 수정하지 않고, get_battery_status() 같은 메서드를 통해 접근하도록 유도
    
- **🔹 상속**
    
    ✅ Robot클래스를 기반으로 MobileRobot, Cobot이 상속받아 기능을 확장함.
    
    ✅ 중복 코드 없이 operate() 같은 메서드를 하위 클래스에서 오버라이딩하여 사용
    
- **🔹 다형성**
    
    ✅ operate() 메서드가 Robot 클래스에 정의되어 있지만, MobileRobot과 Cobot에서 각기 다르게 구현됨.
    
    ✅ 동일한 operate() 메서드를 호출하더라도, 객체 타입에 따라 동작 방식이 달라짐.
    
- **🔹 추상화**
    
    ✅ Robot 클래스는 operate() 같은 공통 인터페이스를 제공하지만, 세부 구현은 각 로봇이 담당
    
    ✅ Sensor, BatteryManager 등도 내부 동작 방식을 숨기고, 필요한 기능만 노출
    


### 🅱️ SOLID 원칙 적용

- **🔹 단일 책임 원칙 (SRP)**
    
    : 클래스는 단 하나의 책임만 가져야 함
    
    ✅ MobileRobot, Cobot, Sensor, BatteryManager, Logger 등 역할을 명확히 나눔
    
- **🔹 개방-폐쇄 원칙 (OCP)**
    
    : 확장에는 열려 있고, 변경에는 닫혀 있어야 함
    
    ✅ 다형성을 활용하여 `operate(n_times=None)`처럼 선택적 매개변수를 지원
    
    ✅ 새로운 기능을 추가할 때 기존 코드를 수정하지 않고 확장 가능하도록 설계
    
    ✅ BatteryManager, Sensor 등을 별도 클래스로 만들어 새로운 방식으로 확장 가능
    
- **🔹 리스코프 치환 원칙 (LSP)**
    
    : 자식 클래스는 부모 클래스의 기능을 변경하지 않고 확장해야 함
    
    ✅ Robot 클래스가 있고, 이를 상속한 MobileRobot, Cobot이 있음
    
    ✅ operate() 메소드를 다형적으로 활용하여 상위 클래스의 인터페이스를 변경하지 않고 기능 확장
    
- **🔹 인터페이스 분리 원칙 (ISP)**
    
    : 하나의 거대한 인터페이스보다 작은 여러 개의 인터페이스로 나누어야 함
    
    ✅ Robot 인터페이스를 거대한 하나의 클래스로 만들지 않고, MobileRobot, Cobot 등으로 나눔
    
    ✅ Sensor, BatteryManager 와 같은 독립적인 클래스로 기능을 모듈화하여 필요 없는 의존성을 최소화
    

## **3️⃣ 코드 예시**


### ✅ **1. 장애물 감지 및 협동 로봇 호출**

```python
if self.sensor.detect_obstacle():
    print("Obstacle detected! Calling the cobot.")  
    self.handle_obstacle()

```

### ✅ **2. 배터리 부족 시 자동 충전**

```python
if self.battery.is_low():
    print("Low battery! Moving to charging station.")  
    self.move_to_charging_station()

```

### ✅ **3. 객체 간 협력 (Cobot 연결)**

```python
amr = MobileRobot("001", "AMR-1", "Jackal")
ur10 = Cobot("002", "Cobot-1", "Universal Robots", joint_count=6)

amr.set_cobot(ur10)  # 협동 로봇 연결

```

## 📌 추가 기능 및 개선점

---

- 의존성 역전 원칙 (DIP)을 만족하도록 인터페이스 클래스 추가
- 장애물의 개수 및 위치를 랜덤하게 생성하는 기능 추가 가능
- RGB 및 Depth 카메라 센서 연결 및 장애물 판단 기준 수정
