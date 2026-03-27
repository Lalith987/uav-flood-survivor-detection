import cv2
import time
from ultralytics import YOLO

# CONFIGURATION

CAMERA_INDEX = 0
MODEL_PATH = "model/path/best.pt"

CONF_THRESHOLD = 0.4
PRINT_INTERVAL = 1.0
ALTITUDE_LABEL = "15–20 m (Low Altitude)"


# LOAD MODEL

model = YOLO(MODEL_PATH)
class_names = model.names

print("✅ YOLOv8 model loaded - yolo_stream.py:20")


# OPEN CAMERA (Linux V4L2)

cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_V4L2)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

if not cap.isOpened():
    raise RuntimeError("❌ Camera could not open")

print("✅ Camera opened successfully - yolo_stream.py:34")


# FPS + PRINT TIMER

prev_time = time.time()
last_print_time = time.time()
fps = 0
alpha = 0.9


# MAIN LOOP

while True:
    ret, frame = cap.read()

    if not ret:
        print("⚠ Frame not received - yolo_stream.py:51")
        break

    # YOLO Inference
    results = model(frame, conf=CONF_THRESHOLD, verbose=False)

    total_detections = 0
    class_counts = {}

    if results[0].boxes is not None:

        for box in results[0].boxes:
            conf = float(box.conf)
            cls_id = int(box.cls)
            label = class_names[cls_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Count detections
            total_detections += 1
            class_counts[label] = class_counts.get(label, 0) + 1

            # Draw Bounding Box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Draw Label
            text = f"{label} {conf:.2f}"
            cv2.putText(frame, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)


    # FPS CALCULATION

    curr_time = time.time()
    instant_fps = 1 / max(curr_time - prev_time, 1e-6)
    fps = alpha * fps + (1 - alpha) * instant_fps
    prev_time = curr_time

    # FPS ON SCREEN
    cv2.putText(frame, f"FPS: {fps:.1f}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # ALTITUDE DISPLAY
    cv2.putText(frame, f"Altitude: {ALTITUDE_LABEL}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)


    # TERMINAL PRINT (CONTINUOUS)

    if curr_time - last_print_time >= PRINT_INTERVAL:

        if total_detections > 0:
            summary = " | ".join([f"{k}: {v}" for k, v in class_counts.items()])
            print(f"Detections: {total_detections} | {summary} | Altitude: {ALTITUDE_LABEL} - yolo_stream.py:104")
        else:
            print("Detections: 0 - yolo_stream.py:106")

        last_print_time = curr_time


    # SHOW WINDOW

    cv2.imshow("YOLOv8 Drowning Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# CLEANUP

cap.release()
cv2.destroyAllWindows()
