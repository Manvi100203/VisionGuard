import time

from src.monitoring.alerts import unknown_face_alert
from src.monitoring.logger import EventLogger


class MonitoringEngine:
    def __init__(self, config):
        self.log_events = config.get("log_events", True)
        self.unknown_face_alert = config.get("unknown_face_alert", True)
        self.logger = EventLogger() if self.log_events else None
        self.last_time = time.time()
        self.fps = 0.0

    def process(self, recognitions, objects):
        now = time.time()
        delta = now - self.last_time
        self.last_time = now

        if delta > 0:
            self.fps = 1 / delta

        if self.unknown_face_alert and unknown_face_alert(recognitions):
            if self.logger:
                self.logger.log("Unknown face detected")

        if self.logger:
            for obj in objects:
                self.logger.log(
                    f"Object detected: {obj['label']} "
                    f"({obj['confidence']:.2f})"
                )
