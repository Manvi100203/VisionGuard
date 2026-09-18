import face_recognition


def encode_image(image):
    locations = face_recognition.face_locations(image, model="hog")
    encodings = face_recognition.face_encodings(image, locations)
    return encodings
