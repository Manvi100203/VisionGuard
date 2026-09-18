import cv2


class CameraStream:
    def __init__(self, index=0, width=1280, height=720):
        self.capture = cv2.VideoCapture(index)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        if not self.capture.isOpened():
            raise RuntimeError("Could not open camera.")

    def read(self):
        return self.capture.read()

    def release(self):
        self.capture.release()
