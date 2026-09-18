import numpy as np
from src.face_detection.detector import FaceDetector


def test_face_detector_returns_list():
    detector = FaceDetector()
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    result = detector.detect(frame)
    assert isinstance(result, list)
