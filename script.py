import cv2
import torch
import time

# Load YOLOv5 model
def load_model():
    print("Loading YOLOv5 traffic light recognition model...")
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # Load YOLOv5s model
    return model

# Detect the traffic light state
def detect_traffic_light(frame, model):
    results = model(frame)  # Perform detection on the frame
    detections = results.pandas().xyxy[0]  # Get detections as pandas DataFrame

    # Iterate over detections to find traffic lights
    for _, detection in detections.iterrows():
        if detection['name'] == 'traffic light':  # Check for traffic light label
            x1, y1, x2, y2 = int(detection['xmin']), int(detection['ymin']), int(detection['xmax']), int(detection['ymax'])
            traffic_light = frame[y1:y2, x1:x2]  # Crop the traffic light region

            # Placeholder: Assume "Red" (you can add color detection logic here)
            return "Red"

    return None

# Simulate traffic light timing (mock data for simplicity)
def get_light_timing():
    return {"Red": 10, "Yellow": 3, "Green": 0}

# Countdown timer
def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i} seconds")
        time.sleep(1)
    print("Light is now green!")

def main():
    # Load the YOLOv5 model
    model = load_model()

    # Start the camera
    camera = cv2.VideoCapture(0)  # Use 0 for live camera; replace with video path if testing on a video file

    try:
        while True:
            ret, frame = camera.read()
            if not ret:
                print("Failed to capture frame. Exiting...")
                break

            # Detect the traffic light state
            light_state = detect_traffic_light(frame, model)
            if light_state:
                print(f"Traffic light detected: {light_state}")

                # Get timing data for the traffic light
                timing = get_light_timing()

                if light_state == "Red":
                    print("Red light detected. Starting countdown...")
                    countdown_timer(timing["Red"])

            # Show the video feed with detections
            results = model(frame)  # Detect objects in the frame
            results.render()  # Add detection boxes to the frame
            cv2.imshow("Traffic Light Detection", results.imgs[0])

            # Break on key press (e.g., 'q')
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()