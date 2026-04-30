Simple Architechture
Camera (Laptop)
     ↓
Python (OpenCV)
     ↓ (Serial)
ESP32
     ↓
Servo Motors

SYSTEM FLOW
Laptop Camera → Python (OpenCV) → Detect Color → Send "1" or "0" → ESP32 → Move Arm


Step 1: #Install the Python CV library
pip install opencv-python pyserial

Step 2: #Run the Python file
python3 cloth_detection.py
