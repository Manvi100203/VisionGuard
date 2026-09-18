from pathlib import Path
import cv2
import yaml

from src.camera.camera_stream import CameraStream
from src.face_detection.detector import FaceDetector
from src.face_recognition.recognizer import FaceRecognizer
from src.object_detection.detector import ObjectDetector
from src.monitoring.monitor import MonitoringEngine
from src.visualization.display import draw_results


def load_config():
    with open(Path("config/config.yaml"), "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main():
    config = load_config()

    camera = CameraStream(
        index=config["camera"]["index"],
        width=config["camera"]["width"],
        height=config["camera"]["height"],
    )
    face_detector = FaceDetector()
    face_recognizer = FaceRecognizer(
        tolerance=config["face_recognition"]["tolerance"],
        model=config["face_recognition"]["model"],
    )
    object_detector = ObjectDetector(
        model_name=config["object_detection"]["model"],
        confidence=config["object_detection"]["confidence"],
    )
    monitor = MonitoringEngine(config["monitoring"])

    print("VisionGuard started. Press Q to quit.")

    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                print("Unable to read camera frame.")
                break

            faces = face_detector.detect(frame)
            recognitions = face_recognizer.recognize(frame, faces)
            objects = object_detector.detect(frame)

            monitor.process(recognitions, objects)
            output = draw_results(
                frame,
                faces,
                recognitions,
                objects,
                monitor.fps,
            )

            cv2.imshow("VisionGuard - Real-Time Monitoring", output)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
