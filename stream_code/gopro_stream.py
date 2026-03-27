import cv2

# Try different camera indices (0, 1, 2, etc.) to find the USB camera
# 0 is usually the default/integrated camera.
camera_index = 0
cap = cv2.VideoCapture(camera_index)

# Check if the camera opened successfully
if not cap.isOpened():
    print(f"Error: Could not open video device at index {camera_index}")
    # You can iterate through indices 0-9 to find the correct one if needed
    # (see Stack Overflow link for script example)
else:
    print(f"Successfully opened camera at index {camera_index}")

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image")
        break

    # Display the resulting frame
    cv2.imshow('USB Webcam Feed', frame)

    # Press 'q' on the keyboard to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
