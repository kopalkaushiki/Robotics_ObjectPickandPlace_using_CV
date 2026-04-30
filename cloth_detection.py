import cv2
import time

cap = cv2.VideoCapture(0)

last_detection_time = 0
detection_interval = 4  # seconds

# Store last detected box
box = None
label = "No Cloth"

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = (35, 40, 40)
    upper = (85, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)

    cv2.imshow("Mask", mask)

    current_time = time.time()

    # Run detection every 5 sec
    if current_time - last_detection_time > detection_interval:

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        found = False

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area > 1500:
                x, y, w, h = cv2.boundingRect(cnt)
                box = (x, y, w, h)
                label = "Cloth Detected"
                found = True
                break

        if not found:
            box = None
            label = "No Cloth Detected"

        print(label)
        last_detection_time = current_time

    # DRAW BOX EVERY FRAME (this was missing before)
    if box is not None:
        x, y, w, h = box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, label, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()