class Logger:
    def log_debug(self, name, message: str):
        print(f"[DEBUG] {name}: {message}")

    def log_info(self, name, message: str):
        print(f"[INFO] {name}: {message}")


'''    
    def log_debug(self, message):
        """ 디버깅 로그 출력 """
        print("-" * 5)
        print(f'[DEBUG] {self.name}: {message}')

    def log_info(self):
        """ 로봇 상태 정보 출력 """
        print("=" * 50)
        print(f"[INFO] Robot<{self.robot_id}> [{self.name}] (Model={self.model})", end="")

'''