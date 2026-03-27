# UAV Edge-AI Flood Survivor Detection using YOLOv8
YOLOv8 | Computer Vision | Disaster AI | Python | OpenCV

## Overview
This project presents a real-time flood survivor detection system using the YOLOv8 object detection model. The system detects humans in flood environments and classifies them into two categories: **Drowning** and **Safety**. The goal is to support disaster response teams by enabling faster identification of survivors using computer vision and edge-AI techniques.

## Features
- Real-time human detection using YOLOv8
- Custom dataset creation and annotation
- Drowning vs Safety classification
- Real-time video detection using OpenCV
- Performance evaluation using Precision, Recall and mAP
- Lightweight model suitable for edge deployment

## Technologies Used

### Programming
- Python

### AI / Computer Vision
- YOLOv8
- OpenCV
- Object Detection
- Deep Learning

### Tools
- LabelImg
- Ultralytics YOLO
- NumPy
- Matplotlib

### Platforms
- Linux
- Windows

## Dataset
A custom dataset was created due to the lack of suitable public datasets.

Dataset characteristics:
- Images collected from open sources
- Manual annotation using LabelImg
- YOLO annotation format
- Two classes:
  - Drowning
  - Safety

Annotation format:

<class_id> <x_center> <y_center> <width> <height>

## Model Training

Model used:
YOLOv8n (lightweight model)

Training configuration:
- Image size: 640×640
- Epochs: 100–200
- Batch size: 4
- Optimizer: Adam
- Learning rate: 0.01

## Performance Metrics

Model evaluated using:

- Precision
- Recall
- mAP@50
- mAP@50-95
- Confusion Matrix

Example results:

Precision: ~0.88  
Recall: ~0.87  
mAP@50: ~0.89  

## Installation

Clone repository:

git clone https://github.com/lalith987/uav-flood-survivor-detection.git

cd uav-flood-survivor-detection

Install dependencies:

pip install -r requirements.txt

## Usage

Run detection:

python detect.py

Run real-time detection:

python yolo_stream.py

## Applications

- Flood rescue operations
- Disaster management
- UAV monitoring
- Emergency response systems
- AI surveillance applications

## Future Improvements

- Larger dataset expansion
- Multi-altitude detection
- Edge device deployment
- UAV hardware integration
- Model optimization

## Results
<img width="630" height="337" alt="2026-02-01 09_41_32-kali linux" src="https://github.com/user-attachments/assets/d524ff14-63bd-4e2a-928d-03981081c341" />
<img width="1024" height="943" alt="Image_3sryrt3sryrt3sry" src="https://github.com/user-attachments/assets/520e8adb-3d67-4c09-89ac-cd68eba7bd21" />
<img width="1024" height="935" alt="Image_8s5hv28s5hv28s5h" src="https://github.com/user-attachments/assets/b1e74fb1-e447-420f-b22d-6b8b22436203" />
<img width="1024" height="923" alt="Image_hf4j6zhf4j6zhf4j" src="https://github.com/user-attachments/assets/46c1a468-bd6a-47de-b19a-722315ed192c" />
![2024-10-15-07-20-24_mp4-0020_jpg rf 0955a3eed62e4d53d0469bb665d5bb58](https://github.com/user-attachments/assets/5c4ca817-3e12-413c-9645-63bcedc8341e)


## Author

Lalith Kumar J  
Cybersecurity & AI Enthusiast 
