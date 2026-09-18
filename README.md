# 🛡️ VisionGuard

### 🔍 Real-Time Face Detection • Face Recognition • Object Detection

<p align="center">

**A Smart Computer Vision Monitoring System**

<img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
<img src="https://img.shields.io/badge/YOLO-Object%20Detection-111111?style=for-the-badge" />

</p>

---

## 👩‍🎓 Student Information

| Detail                  | Information                                       |
| ----------------------- | ------------------------------------------------- |
| **Name**                | **Manvi**                                   |
| **Registration Number** | **`24BAI10510**                    |
| **Program**             | B.Tech — Computer Science & Engineering (AI & ML) |
| **University**          | VIT Bhopal University                             |
| **Project Title**       | VisionGuard                                       |
| **Project Type**        | Academic / Build Your Own Project                 |

---

# 🌟 About VisionGuard

**VisionGuard** is a real-time computer vision monitoring system that combines:

> 👤 **Face Detection** + 🧑‍💻 **Face Recognition** + 🎯 **Object Detection** + 📊 **Monitoring**

The system processes a live camera feed and analyzes each frame to identify faces, recognize registered individuals, detect objects, and provide real-time visual monitoring information.

VisionGuard follows a **modular architecture**, where camera handling, face detection, face recognition, object detection, monitoring, visualization, and testing are implemented as separate components.

---

# 🎯 Problem Statement

Traditional camera monitoring often requires continuous human observation.

This can become:

* ⏳ Time-consuming
* 👀 Difficult to monitor continuously
* 📈 Difficult to scale
* ⚠️ Prone to missed events

**VisionGuard** aims to provide an automated computer-vision based monitoring approach by analyzing live video streams and presenting meaningful detection and recognition results to the user.

---

# 🚀 Objectives

The major objectives of VisionGuard are:

* 📹 Capture live video from a camera.
* 👤 Detect faces in real time.
* 🔍 Recognize registered individuals.
* ❓ Identify unrecognized faces as **Unknown**.
* 🎯 Detect objects present in the camera feed.
* 🖼️ Display bounding boxes and labels.
* 🚨 Generate monitoring events.
* 📝 Maintain event logs.
* ⚙️ Provide configurable detection parameters.
* 🧩 Maintain clean and modular source code.
* 🧪 Provide testing for important components.

---

# ✨ Key Features

| Feature                 | Description                           |
| ----------------------- | ------------------------------------- |
| 👤 **Face Detection**   | Detects faces from live camera frames |
| 🔍 **Face Recognition** | Identifies registered individuals     |
| ❓ **Unknown Detection** | Labels unrecognized faces             |
| 🎯 **Object Detection** | Detects objects using YOLO            |
| 📹 **Live Monitoring**  | Processes camera frames continuously  |
| 🚨 **Alerts**           | Handles monitoring events             |
| 📝 **Event Logging**    | Stores monitoring events              |
| ⚙️ **Configuration**    | Adjustable camera/model settings      |
| 📊 **FPS Monitoring**   | Displays processing performance       |
| 🧪 **Testing**          | Automated component tests             |

---

# 🧠 How VisionGuard Works

```text
                    📹 CAMERA
                       │
                       ▼
               ┌───────────────┐
               │ Frame Capture │
               └───────┬───────┘
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
   👤 FACE DETECTION         🎯 OBJECT DETECTION
          │                         │
          ▼                         ▼
   🔍 FACE RECOGNITION       📊 OBJECT ANALYSIS
          │                         │
          └────────────┬────────────┘
                       │
                       ▼
              🛡️ MONITORING ENGINE
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
      🖥️ VISUALIZATION      📝 EVENT LOGGER
             │                   │
             └─────────┬─────────┘
                       ▼
                🔄 NEXT FRAME
```

---

# 🔄 System Workflow

```text
START
  │
  ▼
Initialize Camera
  │
  ▼
Capture Frame
  │
  ├───────────────┬────────────────
  ▼               ▼
Detect Faces   Detect Objects
  │               │
  ▼               ▼
Recognize       Analyze
Faces           Objects
  │               │
  └───────┬───────┘
          ▼
   Monitoring Engine
          │
     ┌────┴────┐
     ▼         ▼
 Display      Log
 Results      Events
     │
     ▼
Next Frame
     │
     └──────────► Repeat
```

---

# 🧩 Major Functional Modules

## 1️⃣ Face Detection Module

The face detection module identifies human faces present in each camera frame.

### Input

```text
Live Camera Frame
```

### Processing

```text
Frame → Grayscale → Face Detection
```

### Output

```text
Face Bounding Boxes
```

---

## 2️⃣ Face Recognition Module

The recognition module compares detected faces with registered face encodings.

### Input

```text
Detected Face
```

### Processing

```text
Detected Face
      ↓
Face Encoding
      ↓
Compare with Known Encodings
      ↓
Find Closest Match
```

### Output

```text
Person Name
     OR
Unknown
```

---

## 3️⃣ 🎯 Object Detection & Monitoring Module

The object detection module uses a YOLO-based model to identify objects in the camera frame.

### Output

```text
Object
Confidence Score
Bounding Box
```

These results are passed to the monitoring engine for further processing and logging.

---

# 🛠️ Technology Stack

### 💻 Programming

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white)

### 👁️ Computer Vision

![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square\&logo=opencv\&logoColor=white)

### 🧑‍💻 Face Recognition

`face_recognition`

### 🎯 Object Detection

`Ultralytics YOLO`

### 🔢 Numerical Processing

`NumPy`

### ⚙️ Configuration

`PyYAML`

### 🧪 Testing

`Pytest`

### 🌐 Version Control

`Git + GitHub`

---

# 🏗️ Project Architecture

```text
VisionGuard/
│
├── 📄 README.md
├── 📄 statement.md
├── 📄 requirements.txt
├── 📄 LICENSE
├── 📄 .gitignore
│
├── ⚙️ config/
│   └── config.yaml
│
├── 📊 data/
│   ├── dataset/
│   └── known_faces/
│
├── 📐 diagrams/
│
├── 📚 docs/
│   ├── architecture.md
│   ├── dataset.md
│   ├── design-decisions.md
│   ├── functional-requirements.md
│   ├── model-selection.md
│   ├── non-functional-requirements.md
│   ├── objectives.md
│   ├── problem-statement.md
│   ├── references.md
│   ├── testing.md
│   └── workflow.md
│
├── 🤖 models/
│
├── 📓 notebooks/
│
├── 📸 screenshots/
│
├── 💻 src/
│   ├── main.py
│   │
│   ├── 📹 camera/
│   │   └── camera_stream.py
│   │
│   ├── 👤 face_detection/
│   │   ├── detector.py
│   │   └── utils.py
│   │
│   ├── 🔍 face_recognition/
│   │   ├── database.py
│   │   ├── embeddings.py
│   │   └── recognizer.py
│   │
│   ├── 🎯 object_detection/
│   │   ├── detector.py
│   │   └── labels.py
│   │
│   ├── 🛡️ monitoring/
│   │   ├── alerts.py
│   │   ├── logger.py
│   │   └── monitor.py
│   │
│   └── 🖥️ visualization/
│       └── display.py
│
└── 🧪 tests/
    ├── test_face_detection.py
    ├── test_monitoring.py
    └── test_object_detection.py
```

---

# 💻 Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/VisionGuard.git
```

```bash
cd VisionGuard
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 👤 Register Known Faces

Create folders inside:

```text
data/known_faces/
```

Example:

```text
known_faces/
│
├── PersonA/
│   └── image.jpg
│
├── PersonB/
│   └── image.jpg
│
└── PersonC/
    └── image.jpg
```

The folder name represents the person's identity.

For example:

```text
data/known_faces/Manvi/image.jpg
```

will associate the detected face with:

```text
Manvi
```

> 🔐 Only use images for which you have appropriate permission and consent.

---

# ▶️ Run VisionGuard

From the project root:

```bash
python -m src.main
```

The application will:

```text
📹 Open Camera
      ↓
👤 Detect Faces
      ↓
🔍 Recognize Faces
      ↓
🎯 Detect Objects
      ↓
🛡️ Monitor Events
      ↓
🖥️ Display Results
```

To stop the application:

```text
Press Q
```

---

# ⚙️ Configuration

Configuration is available at:

```text
config/config.yaml
```

Example:

```yaml
camera:
  index: 0
  width: 1280
  height: 720

face_recognition:
  tolerance: 0.50
  model: "hog"

object_detection:
  model: "yolo11n.pt"
  confidence: 0.40

monitoring:
  log_events: true
  show_fps: true
  unknown_face_alert: true
```

---

# 🧪 Testing

VisionGuard uses **Pytest** for automated testing.

Run:

```bash
pytest -q
```

Current tests cover:

```text
✓ Face detector output
✓ Monitoring engine initialization
✓ Object detection result structure
```

Additional system-level testing can be performed using real camera input and controlled test scenarios.

---

# 📊 Evaluation Methodology

The project can be evaluated using:

### 👤 Face Detection

* Detection success rate
* False detections
* Performance under different lighting conditions

### 🔍 Face Recognition

* Recognition accuracy
* Unknown-face identification
* Recognition distance/tolerance

### 🎯 Object Detection

* Detection confidence
* Precision
* Recall
* Detection performance

### ⚡ System Performance

* FPS
* Processing latency
* Camera stability
* Resource utilization

> Actual experimental values should be added after testing the final implementation.

---

# 📸 Screenshots

Project screenshots can be added inside:

```text
screenshots/
```

Recommended screenshots:

```text
📸 dashboard.png
📸 face-recognition.png
📸 object-detection.png
📸 monitoring-alert.png
```

Example:

```markdown
## 📸 Results

### 🖥️ Real-Time Monitoring
![VisionGuard Dashboard](screenshots/dashboard.png)

### 👤 Face Recognition
![Face Recognition](screenshots/face-recognition.png)

### 🎯 Object Detection
![Object Detection](screenshots/object-detection.png)
```

---

# 🔐 Privacy & Responsible Use

VisionGuard processes facial information and should therefore be used responsibly.

* 🔒 Use face images only with appropriate authorization.
* 🚫 Do not upload private facial datasets to a public repository.
* 📁 Keep sensitive data locally where appropriate.
* 🏫 Use the system only in permitted environments.
* 📜 Follow applicable institutional policies and laws.
* 👥 Inform participants when required.

---

# ⚠️ Current Limitations

The current implementation has several limitations:

* Recognition performance may vary with lighting and pose.
* Face recognition requires suitable reference images.
* Real-time performance depends on hardware.
* Object detection depends on the selected pretrained model.
* The current system is an academic prototype and is not intended as a production surveillance platform.

---

# 🔮 Future Enhancements

Future versions of VisionGuard could include:

* 🌐 Web-based monitoring dashboard
* 📹 Multi-camera support
* 🧠 Improved face-recognition models
* 🎯 Custom object-detection training
* 🗄️ Database-backed event storage
* 📧 Email notifications
* 🔔 Real-time alerts
* 👥 Role-based authentication
* 📊 Advanced analytics
* ☁️ Cloud deployment
* ⚡ GPU optimization
* 📱 Mobile monitoring application

---

# 📚 Documentation

Detailed documentation is available in the `docs/` directory.

| Document                         | Description               |
| -------------------------------- | ------------------------- |
| `problem-statement.md`           | Project problem           |
| `objectives.md`                  | Project objectives        |
| `functional-requirements.md`     | Functional requirements   |
| `non-functional-requirements.md` | Quality requirements      |
| `architecture.md`                | System architecture       |
| `workflow.md`                    | System workflow           |
| `dataset.md`                     | Dataset description       |
| `model-selection.md`             | Model selection rationale |
| `design-decisions.md`            | Design decisions          |
| `testing.md`                     | Testing methodology       |
| `references.md`                  | References                |

---

# 📐 Design Artifacts

The project includes space for the following diagrams:

```text
📐 System Architecture Diagram
🔄 Workflow Diagram
👥 Use Case Diagram
📦 Component Diagram
🧩 Class Diagram
🔗 Sequence Diagram
```

These diagrams support the design and documentation requirements of the project.

---

# 📈 Project Highlights

```text
┌───────────────────────────────────────────┐
│              🛡️ VISIONGUARD              │
├───────────────────────────────────────────┤
│                                           │
│  👤 Face Detection                        │
│  🔍 Face Recognition                      │
│  🎯 Object Detection                      │
│  📹 Real-Time Monitoring                  │
│  🚨 Event Detection                       │
│  📝 Event Logging                          │
│  ⚙️ Configurable Architecture             │
│  🧪 Automated Testing                      │
│                                           │
└───────────────────────────────────────────┘
```

---

# 🎓 Academic Project

This project has been developed as an academic **Build Your Own Project** and follows the specified requirements for:

* Problem understanding
* Functional requirements
* Non-functional requirements
* System architecture
* Design diagrams
* Modular implementation
* Testing
* Documentation
* GitHub version control

The project documentation also covers dataset description, model selection, and evaluation methodology as applicable to a computation/ML-oriented project.

---



<p align="center">

### 🛡️ VisionGuard

**See. Recognize. Detect. Monitor.**

</p>
