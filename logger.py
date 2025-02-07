class Logger:
    def log_debug(self, name, message: str):
        print(f"[DEBUG] {name}: {message}")

    def log_info(self, name, message: str):
        print(f"[INFO] {name}: {message}")