from datetime import datetime
from pathlib import Path
import csv


class EventLogger:
    def __init__(self, path="logs/events.csv"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            with self.path.open("w", newline="", encoding="utf-8") as file:
                csv.writer(file).writerow(["timestamp", "event"])

    def log(self, event):
        with self.path.open("a", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow([
                datetime.now().isoformat(timespec="seconds"),
                event,
            ])
