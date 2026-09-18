import cv2
import face_recognition

from src.face_recognition.database import FaceDatabase


class FaceRecognizer:
    def __init__(self, tolerance=0.5, model="hog"):
        self.tolerance = tolerance
        self.model = model
        self.database = FaceDatabase(model=model)
        self.database.load()

    def recognize(self, frame, face_boxes):
        results = []
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        for (x, y, w, h) in face_boxes:
            location = [(y, x + w, y + h, x)]
            encodings = face_recognition.face_encodings(rgb, location)

            name = "Unknown"
            distance = None

            if encodings and self.database.encodings:
                distances = face_recognition.face_distance(
                    self.database.encodings, encodings[0]
                )
                best_index = distances.argmin()
                distance = float(distances[best_index])

                if distance <= self.tolerance:
                    name = self.database.names[best_index]

            results.append({
                "box": (x, y, w, h),
                "name": name,
                "distance": distance,
            })

        return results
