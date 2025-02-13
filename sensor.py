import random

class Sensor:
    """ 장애물 감지 센서 """
    def __init__(self, detection_probability=0.2):
        self.detection_probability = detection_probability

    def detect_obstacle(self):
        """ 일정 확률로 장애물 감지 """
        return random.random() < self.detection_probability
