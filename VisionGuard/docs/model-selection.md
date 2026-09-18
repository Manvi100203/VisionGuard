# Model Selection

## Face Detection
OpenCV Haar Cascade is used as a lightweight face-detection component. It is simple to run locally and is suitable for an academic real-time prototype.

## Face Recognition
The `face_recognition` library provides face encodings and distance-based matching against registered faces.

## Object Detection
Ultralytics YOLO is used for real-time object detection. The configured model can be changed in `config/config.yaml`.

## Rationale
The selected components provide a modular combination of traditional computer vision and modern object detection while keeping the project practical for a student implementation.
