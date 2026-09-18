from ultralytics import YOLO


class ObjectDetector:
    def __init__(self, model_name="yolo11n.pt", confidence=0.4):
        self.model = YOLO(model_name)
        self.confidence = confidence

    def detect(self, frame):
        results = self.model.predict(
            source=frame,
            conf=self.confidence,
            verbose=False,
        )

        detections = []
        for result in results:
            if result.boxes is None:
                continue

            names = result.names
            for box in result.boxes:
                xyxy = box.xyxy[0].tolist()
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])

                detections.append({
                    "box": tuple(map(int, xyxy)),
                    "label": names[cls_id],
                    "confidence": conf,
                })

        return detections
