# System Architecture

```text
Camera
  |
  v
Frame Capture
  |
  +------------------+
  |                  |
  v                  v
Face Detector     YOLO Object Detector
  |                  |
  v                  v
Face Recognizer   Object Results
  |                  |
  +--------+---------+
           |
           v
    Monitoring Engine
           |
      +----+----+
      |         |
      v         v
 Visualization  Event Logger
```

The architecture separates input, computer-vision processing, monitoring, and presentation.
