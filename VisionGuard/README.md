# VisionGuard
## Real-Time Face Detection, Recognition & Object Detection Monitoring System

VisionGuard is a modular computer-vision monitoring system designed to process a live camera stream, detect faces, recognize registered people, detect objects, and display monitoring information in real time.

### Major Functional Modules
1. Face Detection
2. Face Recognition
3. Object Detection & Monitoring

### Technologies
- Python
- OpenCV
- NumPy
- Ultralytics YOLO
- face_recognition
- PyYAML
- pytest

### Project Structure
See the repository folders for source code, models, data, tests, documentation, diagrams, screenshots, and evaluation notebooks.

### Installation
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

### Add Known Faces
Place images of registered people inside:
`data/known_faces/<person_name>/image.jpg`

Example:
```text
data/known_faces/
└── Alice/
    └── alice.jpg
```

### Run
```bash
python -m src.main
```

By default, VisionGuard uses webcam index 0. Change settings in `config/config.yaml`.

### Testing
```bash
pytest -q
```

### Documentation
The `docs/` folder contains the problem statement, objectives, requirements, architecture, workflow, dataset/model notes, testing approach, and references.

### Important
This repository is an academic project template/implementation. Face recognition should only be used with appropriate consent and applicable institutional/legal requirements.
