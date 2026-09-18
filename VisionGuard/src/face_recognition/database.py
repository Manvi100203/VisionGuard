from pathlib import Path
import cv2
import face_recognition


class FaceDatabase:
    def __init__(self, directory="data/known_faces", model="hog"):
        self.directory = Path(directory)
        self.model = model
        self.names = []
        self.encodings = []

    def load(self):
        self.names.clear()
        self.encodings.clear()

        if not self.directory.exists():
            return

        for person_dir in sorted(p for p in self.directory.iterdir() if p.is_dir()):
            for image_path in person_dir.iterdir():
                if image_path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
                    continue

                image = cv2.imread(str(image_path))
                if image is None:
                    continue

                rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                locations = face_recognition.face_locations(rgb, model=self.model)
                encodings = face_recognition.face_encodings(rgb, locations)

                if encodings:
                    self.names.append(person_dir.name)
                    self.encodings.append(encodings[0])
