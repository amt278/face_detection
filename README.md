# Face Detection using OpenCV

This project demonstrates how to perform real-time face detection using OpenCV's Haar Cascade Classifier. The program captures video from the webcam (or a video file) and detects faces in the frames, drawing rectangles around detected faces.

## Requirements

- Python 3.x
- OpenCV
- NumPy (optional, but recommended for image processing)

You can install the required libraries using pip:

```bash
pip install opencv-python numpy
```

## Getting Started

1- Run the script:
You can run the script directly in your terminal:

```bash
python face_detection.py
```

2- Capture from webcam:
The script is set up to capture video from the default webcam. If you want to use a video file instead, uncomment the line:

```python
# camera = cv2.VideoCapture("video.mp4")  # capture from video
```
and replace "video.mp4" with the path to your video file.
