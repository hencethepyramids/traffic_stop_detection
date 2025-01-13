# Traffic Light Detection with YOLOv5

This project detects traffic lights in real-time using a live camera feed or video input. It uses [YOLOv5](https://github.com/ultralytics/yolov5) for object detection and identifies the state of the traffic light (e.g., Red, Yellow, Green).

## Features
- Real-time traffic light detection using YOLOv5.
- Countdown timer for red lights.
- Easy-to-run Python script.

## Directory Structure

TRAFFIC_STOP/
- ├── yolov5/          # Cloned YOLOv5 repository
- ├── script.py        # Traffic light detection script
- └── README.md        # Project documentation

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/hencethepyramids/traffic_stop_detection.git
cd traffic_stop_detection
```

### 2. Install Dependencies
```
Navigate to the yolov5 directory and install the required Python packages:

cd yolov5
pip install -r requirements.txt
cd ..
```
### 3. Run the Script

Run the traffic light detection script:

python script.py

4. Test on a Video

If you’d like to test on a video file instead of a live camera feed, modify the camera = cv2.VideoCapture(0) line in script.py to:

camera = cv2.VideoCapture("path_to_video.mp4")

Credits
	•	This project uses the YOLOv5 object detection model by Ultralytics.
	•	YOLOv5 is licensed under the GPL-3.0 License.

License

This project is licensed under the MIT License. See the LICENSE file for details.