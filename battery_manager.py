# 배터리 관리 독립화
# (1) 캡슐화
# (2) 의존성 역전 원칙: MobileRobot은 BatteryManager라는 추상 개념에 의존, BatteryManager의 배터리 관리 세부 방식에 대해서는 신경쓰지 않음

class BatteryManager():
    def __init__(self, init_battery=100):
        # battery 변수 private 선언
        # 정보 은닉, 캡슐화 - 데이터 무결성 보호, 불필요한 변경 방지
        self.__battery = init_battery  # 배터리 100%로 초기화

    def get_battery_status(self):
        """ 배터리 상태 반환 """
        return self.__battery

    def set_battery_status(self, amount: int):
        """ 배터리 상태 설정 """
        if amount < 0:
            print("Error: Battery status cannot be negative.")
            return
        self.__battery = amount
        print(f"Battery status set to {self.__battery}%.")

    def charge(self):
        """ 배터리 충전 """
        self.__battery = 100
        print(f"Battery is fully charged.")

    def discharge(self, amount: int):
        """ 배터리 사용 """
        current_battery = self.get_battery_status()  # 배터리 상태 조회
        if current_battery >= amount:
            self.set_battery_status(current_battery - amount)
        else:
            print(f"Warning: Not enough battery to discharge {amount}%.")
            self.set_battery_status(0)

